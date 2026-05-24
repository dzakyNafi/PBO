import datetime
import pandas as pd
import streamlit as st

from konfigurasi import KATEGORI_PENGELUARAN
from manajer_anggaran import AnggaranHarian
from model import Transaksi


def format_rp(angka):
    return f"Rp {angka or 0:,.0f}".replace(",", ".")


st.set_page_config(
    page_title="Catatan Pengeluaran",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_resource
def get_anggaran_manager():
    return AnggaranHarian()


anggaran = get_anggaran_manager()


def halaman_input(anggaran):
    st.header("Tambah Pengeluaran Baru")

    with st.form("form_transaksi_baru", clear_on_submit=True):
        col1, col2 = st.columns([3, 1])

        with col1:
            deskripsi = st.text_input(
                "Deskripsi*",
                placeholder="Contoh: Makan siang"
            )

        with col2:
            kategori = st.selectbox(
                "Kategori*:",
                KATEGORI_PENGELUARAN,
                index=0
            )

        col3, col4 = st.columns([1, 1])

        with col3:
            jumlah = st.number_input(
                "Jumlah (Rp)*:",
                min_value=0.01,
                step=1000.0,
                format="%.0f",
                value=None,
                placeholder="Contoh: 25000"
            )

        with col4:
            tanggal = st.date_input(
                "Tanggal*:",
                value=datetime.date.today()
            )

        submitted = st.form_submit_button("Simpan Transaksi")

        if submitted:
            if not deskripsi:
                st.warning("Deskripsi wajib diisi.")
            elif jumlah is None or jumlah <= 0:
                st.warning("Jumlah wajib lebih dari 0.")
            else:
                tx = Transaksi(
                    deskripsi,
                    float(jumlah),
                    kategori,
                    tanggal
                )

                if anggaran.tambah_transaksi(tx):
                    st.success("Transaksi berhasil disimpan.")
                    st.cache_data.clear()
                    st.rerun()
                else:
                    st.error("Transaksi gagal disimpan.")


def halaman_riwayat(anggaran):
    st.subheader("Riwayat Transaksi")

    if st.button("Refresh Riwayat"):
        st.cache_data.clear()
        st.rerun()

    df_transaksi = anggaran.get_dataframe_transaksi()

    if df_transaksi is None:
        st.error("Gagal mengambil data riwayat.")
    elif df_transaksi.empty:
        st.info("Belum ada transaksi.")
    else:
        st.dataframe(
            df_transaksi,
            use_container_width=True,
            hide_index=True
        )

        st.divider()
        st.subheader("Hapus Transaksi")
        
        id_hapus = st.number_input(
            "Masukkan ID transaksi yang ingin dihapus:",
            min_value=1,
            step=1
        )
        
        st.warning(f"Pastikan ID {id_hapus} benar sebelum menghapus.")
        
        if st.button("Konfirmasi Hapus Transaksi"):
            if anggaran.hapus_transaksi(int(id_hapus)):
                st.success(f"Transaksi ID {id_hapus} berhasil dihapus.")
                st.cache_data.clear()
                st.rerun()
            else:
                st.error("Gagal menghapus transaksi. ID mungkin tidak ditemukan.")


def halaman_ringkasan(anggaran):
    st.subheader("Ringkasan Pengeluaran")

    col_filter1, col_filter2 = st.columns([1, 2])

    with col_filter1:
        pilihan_periode = st.selectbox(
            "Filter Periode:",
            ["Semua Waktu", "Hari Ini", "Pilih Tanggal"]
        )

        tanggal_filter = None
        label_periode = "(Semua Waktu)"

        if pilihan_periode == "Hari Ini":
            tanggal_filter = datetime.date.today()
            label_periode = f"({tanggal_filter.strftime('%d %b %Y')})"

        elif pilihan_periode == "Pilih Tanggal":
            tanggal_filter = st.date_input(
                "Pilih Tanggal:",
                value=datetime.date.today()
            )
            label_periode = f"({tanggal_filter.strftime('%d %b %Y')})"

    with col_filter2:
        total_pengeluaran = anggaran.hitung_total_pengeluaran(
            tanggal=tanggal_filter
        )

        st.metric(
            label=f"Total Pengeluaran {label_periode}",
            value=format_rp(total_pengeluaran)
        )

    st.divider()
    st.subheader(f"Pengeluaran per Kategori {label_periode}")

    dict_per_kategori = anggaran.get_pengeluaran_per_kategori(
        tanggal=tanggal_filter
    )

    if not dict_per_kategori:
        st.info("Tidak ada data untuk periode ini.")
    else:
        data_kategori = [
            {"Kategori": kategori, "Total": jumlah}

            for kategori, jumlah in dict_per_kategori.items()
        ]

        df_kategori = pd.DataFrame(data_kategori)
        df_kategori["Total (Rp)"] = df_kategori["Total"].apply(format_rp)

        col1, col2 = st.columns(2)

        with col1:
            st.write("Tabel:")
            st.dataframe(
                df_kategori[["Kategori", "Total (Rp)"]],
                hide_index=True,
                use_container_width=True
            )

        with col2:
            st.write("Grafik:")
            st.bar_chart(
                df_kategori.set_index("Kategori")["Total"],
                use_container_width=True
            )


def main():
    st.sidebar.title("Catatan Pengeluaran")
    menu_pilihan = st.sidebar.radio(
        "Pilih Menu:",
        ["Tambah", "Riwayat", "Ringkasan"]
    )

    st.sidebar.markdown("---")
    st.sidebar.info("Jobsheet 11 - Aplikasi Keuangan")

    if menu_pilihan == "Tambah":
        halaman_input(anggaran)
    elif menu_pilihan == "Riwayat":
        halaman_riwayat(anggaran)
    elif menu_pilihan == "Ringkasan":
        halaman_ringkasan(anggaran)

    st.markdown("---")
    st.caption("Pengembangan Aplikasi Berbasis OOP")


if __name__ == "__main__":
    main()