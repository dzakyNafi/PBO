# Praktikum 6: Menambahkan file handling log

import pandas as pd
import folium
import datetime
from abc import ABC, abstractmethod

DEFAULT_LATITUDE = -6.9929
DEFAULT_LONGITUDE = 110.4200
DEFAULT_ZOOM = 13

class Lokasi(ABC):
    def __init__(self, nama: str, latitude: float, longitude: float):
        self.nama = str(nama) if nama else "Tanpa Nama"

        try:
            self.latitude = float(latitude)
            self.longitude = float(longitude)
        except (ValueError, TypeError):
            self.latitude = 0.0
            self.longitude = 0.0

    def get_koordinat(self) -> tuple:
        return (self.latitude, self.longitude)

    @abstractmethod
    def get_info_popup(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.nama} [{type(self).__name__}]"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(nama='{self.nama}', lat={self.latitude:.4f}, lon={self.longitude:.4f})"


class TempatWisata(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, jenis: str, deskripsi: str):
        super().__init__(nama, latitude, longitude)
        self.jenis_wisata = str(jenis)
        self.deskripsi = str(deskripsi)

    def get_info_popup(self) -> str:
        return (
            f"<h4><b>{self.nama}</b></h4>"
            f"<i>{self.jenis_wisata}</i><br><br>"
            f"{self.deskripsi}<br><br>"
            f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})"
        )


class Kuliner(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, menu_andalan: str):
        super().__init__(nama, latitude, longitude)
        self.menu_andalan = str(menu_andalan)

    def get_info_popup(self) -> str:
        return (
            f"<h4><b>{self.nama}</b></h4>"
            f"<i>Kuliner</i><br><br>"
            f"{self.menu_andalan}<br><br>"
            f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})"
        )


class TempatIbadah(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, agama: str, deskripsi: str):
        super().__init__(nama, latitude, longitude)
        self.agama = str(agama)
        self.deskripsi = str(deskripsi)

    def get_info_popup(self) -> str:
        return (
            f"<h4><b>{self.nama}</b></h4>"
            f"<i>Tempat Ibadah ({self.agama})</i><br><br>"
            f"{self.deskripsi}<br><br>"
            f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})"
        )


class KantorPemerintahan(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, deskripsi: str):
        super().__init__(nama, latitude, longitude)
        self.deskripsi = str(deskripsi) if deskripsi else "Kantor pemerintahan."

    def get_info_popup(self) -> str:
        return (
            f"<h4><b>{self.nama}</b></h4>"
            f"<i>Kantor Pemerintahan</i><br><br>"
            f"{self.deskripsi}<br><br>"
            f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})"
        )


class Museum(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, deskripsi: str):
        super().__init__(nama, latitude, longitude)
        self.deskripsi = str(deskripsi) if deskripsi else "Museum."

    def get_info_popup(self) -> str:
        return (
            f"<h4><b>{self.nama}</b></h4>"
            f"<i>Museum</i><br><br>"
            f"{self.deskripsi}<br><br>"
            f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})"
        )


class TamanKota(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, deskripsi: str):
        super().__init__(nama, latitude, longitude)
        self.deskripsi = str(deskripsi) if deskripsi else "Taman kota."

    def get_info_popup(self) -> str:
        return (
            f"<h4><b>{self.nama}</b></h4>"
            f"<i>Taman Kota</i><br><br>"
            f"{self.deskripsi}<br><br>"
            f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})"
        )


def tulis_log(pesan: str, file_log: str = "proses_peta.log"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open(file_log, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {pesan}\n")
    except IOError as error:
        print(f"ERROR menulis log: {error}")


def baca_data_lokasi(nama_file: str) -> pd.DataFrame | None:
    try:
        tulis_log(f"Membaca file CSV: {nama_file}")
        return pd.read_csv(nama_file)

    except FileNotFoundError:
        pesan = f"File CSV '{nama_file}' tidak ditemukan."
        print(pesan)
        tulis_log(pesan)
        return None

    except Exception as error:
        pesan = f"ERROR membaca CSV: {type(error).__name__} - {error}"
        print(pesan)
        tulis_log(pesan)
        return None


def baca_config_peta(nama_file_config: str = "config_peta.txt") -> tuple:
    try:
        with open(nama_file_config, mode="r", encoding="utf-8") as file:
            baris = file.readlines()

        latitude = float(baris[0].strip())
        longitude = float(baris[1].strip())
        zoom = int(baris[2].strip())

        tulis_log(
            f"Konfigurasi peta berhasil dibaca: lat={latitude}, lon={longitude}, zoom={zoom}"
        )
        return latitude, longitude, zoom

    except (FileNotFoundError, ValueError, IndexError) as error:
        pesan = (
            "Konfigurasi peta gagal dibaca atau tidak valid. "
            "Menggunakan koordinat default Semarang."
        )
        print(pesan)
        tulis_log(f"{pesan} Detail error: {type(error).__name__} - {error}")
        return DEFAULT_LATITUDE, DEFAULT_LONGITUDE, DEFAULT_ZOOM


def buat_objek_lokasi_dari_df(dataframe: pd.DataFrame) -> list:
    list_objek_lokasi = []

    if dataframe is None or dataframe.empty:
        tulis_log("Gagal membuat objek: DataFrame kosong.")
        return list_objek_lokasi

    for index, row in dataframe.iterrows():
        nama = row.get("Nama")
        lat = row.get("Latitude")
        lon = row.get("Longitude")
        tipe = str(row.get("Tipe", "Lainnya")).strip()
        deskripsi = row.get("Deskripsi", "")

        if nama is None or lat is None or lon is None:
            tulis_log(f"Baris {index} dilewati karena data tidak lengkap.")
            continue

        tipe_lower = tipe.lower()
        objek = None

        if "kantor" in tipe_lower or "pemerintahan" in tipe_lower:
            objek = KantorPemerintahan(nama, lat, lon, deskripsi)

        elif "museum" in tipe_lower:
            objek = Museum(nama, lat, lon, deskripsi)

        elif "taman" in tipe_lower:
            objek = TamanKota(nama, lat, lon, deskripsi)

        elif "wisata" in tipe_lower or tipe_lower == "landmark":
            objek = TempatWisata(nama, lat, lon, tipe, deskripsi)

        elif tipe_lower == "kuliner":
            objek = Kuliner(nama, lat, lon, deskripsi)

        elif "ibadah" in tipe_lower:
            objek = TempatIbadah(nama, lat, lon, "Umum", deskripsi)

        else:
            pesan = f"Tipe '{tipe}' pada '{nama}' belum dikenali."
            print(pesan)
            tulis_log(pesan)

        if objek is not None:
            list_objek_lokasi.append(objek)

    tulis_log(f"Berhasil membuat {len(list_objek_lokasi)} objek lokasi.")
    return list_objek_lokasi


def pilih_icon_marker(lokasi: Lokasi) -> folium.Icon:
    if isinstance(lokasi, TempatWisata):
        return folium.Icon(color="blue", icon="camera")
    elif isinstance(lokasi, Kuliner):
        return folium.Icon(color="red", icon="cutlery")
    elif isinstance(lokasi, TempatIbadah):
        return folium.Icon(color="green", icon="home")
    elif isinstance(lokasi, KantorPemerintahan):
        return folium.Icon(color="gray", icon="briefcase")
    elif isinstance(lokasi, Museum):
        return folium.Icon(color="purple", icon="info-sign")
    elif isinstance(lokasi, TamanKota):
        return folium.Icon(color="darkgreen", icon="leaf")
    else:
        return folium.Icon(color="black", icon="info-sign")


def buat_peta_lokasi_folium(
    list_objek: list,
    file_output: str = "peta_interaktif_semarang.html",
    file_config: str = "config_peta.txt"
):
    nama_fungsi = "buat_peta_lokasi_folium"

    if not list_objek:
        pesan = f"[{nama_fungsi}] Gagal: tidak ada lokasi untuk dipetakan."
        print(pesan)
        tulis_log(pesan)
        return

    tulis_log(f"[{nama_fungsi}] Mulai membuat peta: {file_output}")

    lat_tengah, lon_tengah, zoom_awal = baca_config_peta(file_config)

    peta = folium.Map(
        location=[lat_tengah, lon_tengah],
        zoom_start=zoom_awal,
        tiles="OpenStreetMap"
    )

    jumlah_marker = 0
    lokasi_dilewati = []

    for lokasi in list_objek:
        koordinat = lokasi.get_koordinat()

        if koordinat == (0.0, 0.0):
            lokasi_dilewati.append(lokasi.nama)
            continue

        folium.Marker(
            location=koordinat,
            popup=folium.Popup(lokasi.get_info_popup(), max_width=300),
            tooltip=f"{lokasi.nama} - {type(lokasi).__name__}",
            icon=pilih_icon_marker(lokasi)
        ).add_to(peta)

        jumlah_marker += 1

    if lokasi_dilewati:
        tulis_log(f"Lokasi dilewati karena koordinat tidak valid: {', '.join(lokasi_dilewati)}")

    try:
        peta.save(file_output)
        pesan = f"Peta '{file_output}' berhasil dibuat dengan {jumlah_marker} marker."
        print(pesan)
        tulis_log(pesan)

    except Exception as error:
        pesan = f"ERROR menyimpan peta: {type(error).__name__} - {error}"
        print(pesan)
        tulis_log(pesan)


if __name__ == "__main__":
    print("--- Praktikum 6: File Handling Log ---")

    df_lokasi = baca_data_lokasi("lokasi_semarang.csv")
    list_semua_lokasi = buat_objek_lokasi_dari_df(df_lokasi)

    print("\nDaftar objek lokasi yang berhasil dibuat:")
    for nomor, lokasi in enumerate(list_semua_lokasi, start=1):
        print(f"{nomor}. {repr(lokasi)}")

    buat_peta_lokasi_folium(
        list_semua_lokasi,
        "peta_interaktif_semarang.html",
        "config_peta.txt"
    )

    print("Silakan cek file:")
    print("1. peta_interaktif_semarang.html")
    print("2. proses_peta.log")
