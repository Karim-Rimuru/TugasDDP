# buatlah rumus meenghitung luas persegi
sisi = 15
luasPersegi  = sisi * sisi
#cetak
print("\n----------Luas Persegi----------\n")
print("Luas Persegi dengan Sisi",sisi,
      "Luasnya =",luasPersegi,)

# buatlah rumus menghitung luas persegi panjang 
panjang = 16
lebar = 15
luasPrsegiPanjang = panjang * lebar
#cetak
print("\n----------Luas Persegi Panjang----------\n")
print("Luas Persegi Panjang dengan Panjang ",panjang, "dan Lebar", lebar,
      "Luasnya =",luasPrsegiPanjang,)

# buatlah rumus menghitung luas segitiga 
alas = 15
tinggi = 20
luasSegitiga = (alas * tinggi) / 2
#cetak  
print("\n----------Luas Segitiga----------\n")
print("Luas Segita dengan Alas ",alas, "dan Tinggi", tinggi,
      "Luasnya =",luasSegitiga,)

# buatlah rumus menghitung luas Lingkaran
PHI = 3.14
jari2 = 25
luasLingkaran = PHI * jari2 * jari2
#cetak 
print("\n----------Luas Lingkaran----------\n")
print("Luas Lingkaran dengan jari-jari ",jari2,
      "Luasnya =",luasLingkaran,)

# buat perbandingan lebih besar dan lebih kecil dari luas persegi dan luas persegi panjang 
print("\n----------Perbandingan Lebih Besar----------\n")
print("luas persegi lebih besar daripada luas persegi panjang =", luasPersegi > luasPrsegiPanjang)
print("\n----------Perbandingan Lebih Kecil----------\n")
print("luas persegi lebih kecil daripada luas persegi panjang =", luasPersegi < luasPrsegiPanjang)

# buat perbandingan lebih besar dan lebih kecil dari luas Segitiga dan luas Lingkaran 
print("\n----------Perbandingan Lebih Besar----------\n")
print("luas segitiga lebih besar daripada luas lingkaran panjang =", luasSegitiga > luasLingkaran)
print("\n----------Perbandingan Lebih Kecil----------\n")
print("luas segitiga lebih kecil daripada luas lingkaran panjang =", luasSegitiga < luasLingkaran)