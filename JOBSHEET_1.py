#PRAKTIKUM 1
#1. Number (int, float, , complex)
# Integer(int)
angka_int = 10
print("Angka_int = ", angka_int, "->",type(angka_int))

# float
angka_float = 3.14
print("Angka_float = ",angka_float, "->",type(angka_float))

# Complex
angka_complex =  2 + 3
print("Angka_complex = ",angka_complex, "->",type(angka_complex))

#2. Boolean
is_active = True 
print("is_active = ","->",type(is_active))

#3. String
teks = "Hello, Python !"
print("teks = ",teks, "->", type(teks))

#4. List
#List adalah tipe data terurut dan dapat diubah kembali(mutabele1)
daftar_angka = [1,2,3,4,5]
print("daftar_angka = ",daftar_angka, "->", type(daftar_angka) )

#5. Tuple
# Tuple adalah tipe data terurut tapi tidak dapat diubah kembali
koordinat =  (10,20)
print("koordinat = ",koordinat, "->", type(koordinat))

#6. Dictionary
# Dictionary adalah tipe data dalam pasangan key-value
data_mahasiswa = {"nama" : "Andi", "nim" : "All.2022.12345", "jurusan" : "Teknik Informatika"}
print("data_mahasiswa = ",data_mahasiswa, "->", type(data_mahasiswa))

#7. set
#Set adalah tipe data yang tidak terurut,unik (tiap elemen hanya muncul sekali)
himpunan_angka =  {1,2,3,4,1}

#8. Contoh penggunaan konversi tipe data
nilai_str = "100"
print("\nnilai_str + ",nilai_str, "->", type(nilai_str))
nilai_int = int(nilai_str)
print("nilai_int = ",nilai_int, "->", type(nilai_int))

#PRAKTIKUM 2
#-*- coding: utf-8 -*-

#1. Pendeklarasian variabel
nama = "Budi"
umur = 20
tinggi = 170.5
is_student = True

print("",)
print("Nama = ",nama)
print("umur = ", umur)
print("Tinggi = ",tinggi,"cm")
print("Mahasiswa = ",True)

#Python tidak memerlukan dekalrasi tipe data secara explidit.
#Tipe data aka menyeduaikan variabelyang diberikan()

#2.Operasi Aritematika
a =  10
b = 3

penjumlahan = a + b
pengurangan = a - b   
perkalian = a * b
pembagian = a / b
pembagian_bulat = a // b
modulus =a % b
pangkat = a ** b

print("\nOperasi Aritmatika")
print("a = ",a ,"b = ",b)
print("Penjumlahan = ", penjumlahan)
print("Perkalian = ",perkalian )
print("Pembagian = ",pembagian )
print("Pembagian Bulat = ",pembagian_bulat )
print("Modulus = ",modulus )
print("Pengurangan = ",pangkat )
print("Pangkat = ",pengurangan )

#3. Operasi perbandingan
#Menghasilkan nilai Boolean (True/False)
lebih_besar = a > b
kurang_dari = a < b
sama_dengan = a == b
tidak_sama = a != b
lebih_besar_sama = a >= b 
kurang_sama = a <= b 

print("\nOperasi Perbandingan")
print("a > b = ",lebih_besar )
print("a < b = ",kurang_dari)
print("a == b = ",sama_dengan )
print("a != b = ",tidak_sama )
print("a >= b = ",lebih_besar_sama )
print("a <= b = ",kurang_sama )

#4. Operasi Logika 
# and, or , not
x = True
y = False

logika_and = x and y
logika_or = x or y
logika_not_x = not x

print("\nOperasi Logika")
print("x = ",x ,"y = ",y)
print("x and y = ", logika_and)
print("x or y = ", logika_or)
print("not x = ", logika_not_x)

#5. Contoh penggunaan di dalam percabangan
if a > b and b > 0 :
    print("\nKondisi terpenuhi: a lebih besar dari b, dan b masih postif")
else :
    print("\nKondisi tidak terpenuhi atau b <= 0")

#PRAKTIKUM  3
#1. IF sederhana 
# Program hanya mengeksekusi jika bernilai true
nilai = 85
print("Contoh IF sederhana")
if nilai > 80:
    print("Selamat!Anda lulus dengan nilai tinggi.\n")

#2. IF-ELSE
# Jika kondisi bernila True, eksekusi blok IF jika bernilai False eksekusi blok ELSE
umur2 = 17
print("contoh IF-ELSE")
if umur2 >= 18 :
    print("Anda sudah cukup umur untuk mendapatkan SIM")
else :
    print("Anda belum cukup umur untuk mendapatkan SIM")

#3. IF-ELIF-ELSE
# Menangani banyak kondisi secara berurutan
# Jika ada kondisi yang terpenuhi,blok bersangkutan akan dieksekusi,
# lalu program melewati blok kondisi setelahnya 

hari = "rabu"
print("Contoh IF-ELIF-ELSE")
if hari == "Senin" :
    print("Hari Senin - Saatnya kembali bekerja!")
elif hari == "Selasa" : 
    print("Hari Selasa - Jadwal rapat mingguan")
elif hari == "Rabu" :
    print("Hari Rabu - Ada diskon di beberapa toko")
else :
    print("Hari lainnya - Atur jadwalmu dengan baik")

#4. IF bersarang(Nested IF)
# Kondisi di dalam kondisi biasa digunakan jika perlu
# memeriksa sub-kondisi setelah kondisi pertama dipenuhi

suhu = 35
print("Contoh nested IF")
if suhu > 30 :
    print("Cuaca cukup panas")
    if suhu >  40 :
        print("bahkan sangat terik! disarankan banyak minum air.")
    else :
        print("masih relatif normal,tapi tetap jaga kesehatan.")
else :
    print("Cuaca sepertinya cukup sejuk.\n")

#5. Menggabungkan  percabangan dengan Operasi logika 
# Memeriksa beberapa kondisi sekaligus dengand and, or , not

nilai_teori = 75
nilai_praktik = 80

print("Contoh IF dengan operasi logika and.or :")
if nilai_teori >= 70 and nilai_praktik >= 70 :
    print("Anda lulus karena nilai teori dan praktik memadai")
elif nilai_teori < 70 and nilai_praktik < 70 :
    print("Anda perlu meningkatkan nilai teori dan praktik")
elif nilai_teori < 70 :
    print("Anda perlu meningkatkan nilai teori")
else :
    print("Anda perlu meningkatkan nilai praktik")

#6. Penggunaan IF ternary (atau Conditional Expression) 
# Bentuk ringkas : <hasil_if_true> if <kondisi> else <hasil_if_false>

angka = -5
print("Contoh IF Ternary (Conditional Expressions)")
status = "Positif" if angka > 0 else "Negatif atau Nol"
print("Angka = ", angka, "=>", status)

# PRAKTIKUM : PERULANGAN

#1. FOR Loop dengan range()
print("1) FOR loop dengan range()")
for i in range(5) :
    print("Perulangan ke-",i)
# range (5) menghasilkan nilai 0,1,2,3,4,5
# sehingga perulangan akan berjalan sebanyak 5 kali

print() # pemisah output

#2. FOR Loop untuk mengiterasi list
print("2) FOR loop mengiterasi List ")
buah = ["apel","Mangga","Jeruk","Pisang"]
for item in buah :
    print("Buah :",item)

    #Loop akan mengeksekusi setiap elemen dalam list "buah"
print()

#3. WHILE Loop 
print("3) WHILE Loop sederhana")
count = 0
while count < 5 :
    print("count :",count)
    count += 1

#perulangan akan terus dijalankan selama kondisi (count < 5) bernilai True
print()

#4. BREAK pada Loop
print("4) BREAK di dalam Loop")
for x in range(10) :
    if x == 3:
        print("Loop dihentikan pada x =",x)
        break # mengakhiri loop saat i = 3
    print("i =", i)
#Keyword break langsung menghentikan perulangan

#4. CONTINUE pada Loop
print("4) CONTINUE di dalam Loop")
for x in range(10) :
    if x == 2:
        print("Lewati x =", x, "dengan continue")
        continue # melewati iterasi saat ini dan lanjur ke iterasi berikutnya
    print("x =", x)
# Saat i = 2, baris print("i =", i) tidak akan dieksekusi
print()

#5. NESTED Loop (Loop Bersarang)
print("6) Nested Loop")
for i in range(3) :
    for j in range(2) :
        print(f"i = {i}, j = {j} ")
#Pada setiap iterasi i, Loop j akan berjalan dari 0 sampai 1
print()

#6. Memanfaatkan Else pada Loop
print("6) ELSE pada Loop FOR/WHILE")
# Python memiliki fitur unik: blok else pada Loop
# Blook ELSE akan dieksekusi jika Loop selesai tanpa di-break

for c in range(3) :
    print("x = ", x)
    y += 1
else :
    print("Loop for telah selesai tanpa break.\n")

z = 0
while z < 3 :
    print("z = ",z)
    z += 1
else :
    print("Loop while telah selesai tanpa break.\n")

#8. PASS sebagai placeholder
print("8) PASS (placeholder)")
for i in range(3) :
    if i == 1 :
        pass # pass tidak melakukan apa apa digunakan sebagai placeholder
    print("i = ", i)

# PENUGASAN
# MENGHITUNG BMI DAN PENGKATEGORIAN 
massa_tubuh = float(input("masukkan massa tubuh"))
tinggi_tubuh = float(input("masukkan tinggi tubuh(m)"))

hitung_BMI  = massa_tubuh / tinggi_tubuh ** 2
print("BMI = ",hitung_BMI)

if hitung_BMI < 18.5 :
    print("Underweight")
elif hitung_BMI > 18.5 and hitung_BMI < 24.9 :
    print("Normal")
else :
    print("Overweight")

#CEK BILANGAN GENAP, GANJIL, ATAU,PRIMA
bilangan = int(input("Masukkan bilangan"))

if bilangan % 2 == 0 :
    print(bilangan, "bilangan genap")
elif bilangan % 2 != 0 :
    for bil in range(2,bilangan) :
        if bilangan % bil == 0 :
            break
    print(bilangan,"bilangan prima")         