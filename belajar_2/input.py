# Fungsi input itu dianggapnya adalah String, sehingga harus di conver menjadi integer
panjang = input("Berapa Panjang ? ")
panjang = int(panjang)
lebar = input("Berapa Lebar ? ")
lebar = int(lebar)


keliling = 2 * (panjang + lebar)

print(keliling)