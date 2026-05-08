from abc import ABC, abstractmethod
import locale
import random # Untuk simulasi

# Setting locale Indonesia
try:
  locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
except locale.Error:
  print("Locale id_ID.UTF-8 tidak tersedia, gunakan locale default.")

def format_rupiah(angka):
  return locale.currency(angka, grouping=True, symbol='Rp ')

# Kelas Abstrak
class AlatPembayaranAbstrak(ABC):
  def __init__(self, nama_metode):
    self.nama_metode = nama_metode
    print(f"Inisialisasi alat pembayaran: {self.nama_metode}")
  def info(self):
    print(f"Metode Pembayaran: {self.nama_metode}")
  @abstractmethod

  def proses_pembayaran(self, jumlah):
    """
    Metode abstrak untuk memproses pembayaran sejumlah 'jumlah'.
    Harus diimplementasikan oleh subclass.
    Harus mengembalikan True jika berhasil, False jika gagal.
    """
    pass

# --- Implementasi Subclass Konkret ---
# 1. Subclass Konkret Pertama: KartuKredit
class KartuKredit(AlatPembayaranAbstrak):
  def __init__(self, nomor_kartu, nama_pemilik):
    super().__init__("Kartu Kredit")
    self.nomor_kartu = nomor_kartu[-4:] # Simpan 4 digit terakhirsaja
    self.nama_pemilik = nama_pemilik
    print(f" -> Kartu Kredit ************{self.nomor_kartu}({self.nama_pemilik}) siap.")

# Implementasi metode abstrak proses_pembayaran
  def proses_pembayaran(self, jumlah):
    print(f" Memproses pembayaran {format_rupiah(jumlah)} via Kartu Kredit ************{self.nomor_kartu}...")

# Simulasi keberhasilan/kegagalan
    berhasil = random.choice([True, False])
    if berhasil:
      print(" Pembayaran Kartu Kredit Berhasil.")
      return True
    else:
      print(" Pembayaran Kartu Kredit Gagal (Limit tidak cukup/Error).")
      return False

# 2. Subclass Konkret Kedua: DompetDigital
class DompetDigital(AlatPembayaranAbstrak):
  def __init__(self, nomor_telepon, nama_provider):
    super().__init__(f"Dompet Digital ({nama_provider})")
    self.nomor_telepon = nomor_telepon
    self._saldo = random.randint(50000, 500000) # Saldo awal acak
    print(f" -> Dompet Digital {self.nomor_telepon} siap (Saldo: {format_rupiah(self._saldo)}).")

# Implementasi metode abstrak proses_pembayaran
  def proses_pembayaran(self, jumlah):
    print(f" Memproses pembayaran {format_rupiah(jumlah)} via DompetDigital {self.nomor_telepon}...")
    if jumlah <= self._saldo:
      self._saldo -= jumlah
      print(" Pembayaran Dompet Digital Berhasil.")
      print(f" Saldo tersisa: {format_rupiah(self._saldo)}")
      return True
    else:
      print(" Pembayaran Dompet Digital Gagal (Saldo tidakmencukupi).")
      print(f" Saldo saat ini: {format_rupiah(self._saldo)}")
      return False

# --- Kode Utama ---
if __name__ == "__main__":
  print("\nMembuat Objek Alat Pembayaran...")
  kartu_bca = KartuKredit("1234-5678-9012-3456", "Budi Cahyono")
  gopay = DompetDigital("08123456789", "GoPay")
  
  print("\nMelakukan Pembayaran:")
  print("\nMencoba bayar dengan Kartu Kredit:")
  kartu_bca.info()
  status_kk = kartu_bca.proses_pembayaran(150000)
  print(f" Status Transaksi KK: {'Sukses' if status_kk else 'Gagal'}")
  print("\nMencoba bayar dengan GoPay (Jumlah Kecil):")
  gopay.info()
  status_gopay1 = gopay.proses_pembayaran(75000)
  print(f" Status Transaksi GoPay 1: {'Sukses' if status_gopay1 else 'Gagal'}")
  print("\nMencoba bayar dengan GoPay (Jumlah Besar):")
  gopay.info()
  status_gopay2 = gopay.proses_pembayaran(1000000) # Kemungkinan gagal karena saldo
  print(f" Status Transaksi GoPay 2: {'Sukses' if status_gopay2 else 'Gagal'}")