nilai = int(input('Masukan Nilai range 0-100 : '))
if nilai < 0 or nilai > 100:
    print('true : Nilai range 0-100')
    exit()

print('BENAR')


nilai = 80
if nilai > 85:
    print('A')
elif nilai >= 65 and nilai <= 85:
    print('B')