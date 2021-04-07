#menghitung nilai rata rata yang akan diinputkan

# input banyak data
banyak_data = int(input("Anda akan merata-rata berapa data ? :"))

#membuat tempat untuk angka (list)
data_angka = []

i = 1
while i <= banyak_data:
    angka = float(input("Masukkan angka :"))
    data_angka.append(angka)
    i = i + 1

#penghitungan nilai rata-rata dari jumlah data nilai
hasil_ratarata = sum(data_angka)/banyak_data

#menampilkan hasil
print("Nilai rata-rata dari semua data anda adalah : ", hasil_ratarata)