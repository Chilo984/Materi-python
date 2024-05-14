def sapaan():#fungsi tanpa parameter
    print('hello world')
sapaan()
sapaan()
sapaan()
sapaan()

def salam(ucapan):#fungsi menggunakan parameter
    print(ucapan)
salam('selamat siang brooo')

def penjumlahan(a,b):
    hasil = a + b 
    print(hasil)

penjumlahan(50,100)

def luas_persegi_panjang(panjang,lebar):#fungsi yang mengembalikan nilai
    return panjang * lebar
print(luas_persegi_panjang(5,8))

nama = 'Dion senowijaya'

def cetak_string():
    nama()
    print