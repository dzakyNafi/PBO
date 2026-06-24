# Praktikum 4: Membuat objek dari DataFrame Pandasbuat_objek_lokasi

import pandas as pd
from abc import ABC, abstractmethod

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
        return f"<b>{self.nama}</b><br>{self.jenis_wisata}<br>{self.deskripsi}"


class Kuliner(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, menu_andalan: str):
        super().__init__(nama, latitude, longitude)
        self.menu_andalan = str(menu_andalan)

    def get_info_popup(self) -> str:
        return f"<b>{self.nama}</b><br>Kuliner<br>{self.menu_andalan}"


class TempatIbadah(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, agama: str, deskripsi: str):
        super().__init__(nama, latitude, longitude)
        self.agama = str(agama)
        self.deskripsi = str(deskripsi)

    def get_info_popup(self) -> str:
        return f"<b>{self.nama}</b><br>Tempat Ibadah ({self.agama})<br>{self.deskripsi}"


def baca_data_lokasi(nama_file: str) -> pd.DataFrame | None:
    try:
        return pd.read_csv(nama_file)
    except FileNotFoundError:
        print(f"ERROR: File '{nama_file}' tidak ditemukan.")
        return None
    except Exception as error:
        print(f"ERROR: {type(error).__name__} - {error}")
        return None


def buat_objek_lokasi_dari_df(dataframe: pd.DataFrame) -> list:
    list_objek_lokasi = []

    if dataframe is None or dataframe.empty:
        print("DataFrame kosong atau tidak tersedia.")
        return list_objek_lokasi

    for index, row in dataframe.iterrows():
        nama = row.get("Nama")
        lat = row.get("Latitude")
        lon = row.get("Longitude")
        tipe = row.get("Tipe", "Lainnya")
        deskripsi = row.get("Deskripsi", "")

        if nama is None or lat is None or lon is None:
            print(f"Baris {index} dilewati karena data tidak lengkap.")
            continue

        objek = None

        if "Wisata" in tipe or tipe == "Landmark":
            objek = TempatWisata(nama, lat, lon, tipe, deskripsi)

        elif tipe == "Kuliner":
            objek = Kuliner(nama, lat, lon, deskripsi)

        elif "Ibadah" in tipe:
            objek = TempatIbadah(nama, lat, lon, "Umum", deskripsi)

        else:
            print(f"Tipe '{tipe}' pada '{nama}' belum dikenali.")

        if objek is not None:
            list_objek_lokasi.append(objek)

    return list_objek_lokasi


if __name__ == "__main__":
    df_lokasi = baca_data_lokasi("lokasi_semarang.csv")
    list_semua_lokasi = buat_objek_lokasi_dari_df(df_lokasi)

    print("\nDaftar objek yang berhasil dibuat:")
    for nomor, lokasi in enumerate(list_semua_lokasi, start=1):
        print(f"{nomor}. {repr(lokasi)}")