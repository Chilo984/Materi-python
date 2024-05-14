import random

angka_rahasia = random.randint(1,10)
percobaan = 0

while True:
    tebakan = int(input('Masukkan Angka : '))
    if tebakan == angka_rahasia:
        print('Benar')
        print('Selamat kamu telah menebak dalam {percobaan} tebakan')
        break

    elif tebakan <= angka_rahasia:
        print('Rendah men blok')
    elif tebakan >= angka_rahasia:
        print('Keduwuren Wak')
    else:
        exit
    percobaan += 1