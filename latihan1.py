buku = 100000
buku_setelah_diskon = buku - (buku * (40 / 100))


ongkir = 9000
ongkir_tambahan = 3000


total_harga_buku = buku_setelah_diskon * 60

total_ongkir_tambahan = ongkir_tambahan * 59
total_all_ongkir = ongkir + total_ongkir_tambahan

print ("Harga Buku Normal =", buku)
print ("Harga Buku Setelah Diskon per Satuan Buku =", buku_setelah_diskon)
print ("Ongkir Pertama =", ongkir)
print ("Ongkir Selanjutnya =", ongkir_tambahan)
print ("---")
print ("Total Ongkir adalah =", total_all_ongkir)
print ("Total Harga Buku = ", total_harga_buku)
print ("Total Keseluruhan adalah = ", total_harga_buku + total_all_ongkir)