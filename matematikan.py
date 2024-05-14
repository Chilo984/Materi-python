def penjumlahan(a,b):
    return a + b
 
def pengurangan(a,b):
    return a - b

def pembagi(a,b):
    return a / b

def perkalian(a,b):
    return a * b

def tampilan():
    print("1. jumlahan")
    print("2. kurangan")
    print("3. perkalian")
    print("4. pembagian")

def operasi(pilihan):
    if pilihan == 1:
        a = int(input('masukan bilang pertama='))
        b = int(input('masukan bilang kedua='))
        print(a,'+',b,'=',penjumlahan(a,b))
    elif pilihan == 2:
        a = int(input('masukan bilang pertama='))
        b = int(input('masukan bilang kedua='))
        print(a,'-',b,'=',pengurangan(a,b))
    elif pilihan == 3:
        a = int(input('masukan bilang pertama='))
        b = int(input('masukan bilang kedua='))
        print(a,'*',b,'=',perkalian(a,b))
    elif pilihan == 4:
        a = int(input('masukan bilang pertama='))
        b = int(input('masukan bilang kedua='))
        print(a,'/',b,'=',pembagi(a,b))
    else:
        print('pilihan tidak valid')