# Praktikum 3: Membuat kelas OOP untuk lokasi geografis

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
        return (
            f"{type(self).__name__}"
            f"(nama='{self.nama}', lat={self.latitude:.4f}, lon={self.longitude:.4f})"
        )


class TempatWisata(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, jenis: str, deskripsi: str):
        super().__init__(nama, latitude, longitude)
        self.jenis_wisata = str(jenis) if jenis else "Umum"
        self.deskripsi = str(deskripsi) if deskripsi else "Tidak ada deskripsi."

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
        self.menu_andalan = str(menu_andalan) if menu_andalan else "Tidak diketahui"

    def get_info_popup(self) -> str:
        return (
            f"<h4><b>{self.nama}</b></h4>"
            f"<i>Kuliner</i><br><br>"
            f"Menu/Deskripsi: {self.menu_andalan}<br><br>"
            f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})"
        )


class TempatIbadah(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float, agama: str = "Umum", deskripsi: str = ""):
        super().__init__(nama, latitude, longitude)
        self.agama = str(agama) if agama else "Umum"
        self.deskripsi = str(deskripsi) if deskripsi else "Tempat ibadah."

    def get_info_popup(self) -> str:
        return (
            f"<h4><b>{self.nama}</b></h4>"
            f"<i>Tempat Ibadah ({self.agama})</i><br><br>"
            f"{self.deskripsi}<br><br>"
            f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})"
        )


# Kelas baru untuk mini project SIG
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


if __name__ == "__main__":
    lokasi1 = TempatWisata(
        "Lawang Sewu",
        -6.9840,
        110.4105,
        "Wisata Sejarah",
        "Bangunan bersejarah di Semarang."
    )

    lokasi2 = Kuliner(
        "Toko Oen",
        -6.9715,
        110.4235,
        "Es krim dan makanan legendaris."
    )

    lokasi3 = TempatIbadah(
        "Masjid Agung Jawa Tengah",
        -6.9892,
        110.4452,
        "Islam",
        "Masjid besar dengan arsitektur megah."
    )

    lokasi4 = KantorPemerintahan(
        "Balai Kota Semarang",
        -6.9817,
        110.4091,
        "Pusat administrasi Pemerintah Kota Semarang."
    )

    lokasi5 = Museum(
        "Museum Ranggawarsita",
        -6.9854,
        110.3831,
        "Museum sejarah, budaya, dan geologi Jawa Tengah."
    )

    lokasi6 = TamanKota(
        "Taman Indonesia Kaya",
        -6.9912,
        110.4218,
        "Ruang terbuka hijau dan panggung seni budaya."
    )

    print(lokasi1)
    print(lokasi2)
    print(lokasi3)
    print(lokasi4)
    print(lokasi5)
    print(lokasi6)

    print(lokasi1.get_info_popup())
