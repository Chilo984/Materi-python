string1 = 'Hello'
string2 = 'World'
int1 = 5
print(string1 + " " + string2)
print((string1 + " ") * 20) 
print(string1 + str(int1))

list_kalimat = ['Aku','seorang','Kapiten']
kalimat = " ".join(list_kalimat)
print(kalimat)

list_kalimat1 = 'Aku Programmer handal'
kalimat1 = list_kalimat1.split()
print(kalimat1)

kalimat2 =list_kalimat1.replace('handal','hebat')
print(kalimat2)

nama = 'dion senowijaya'
nama1 = 'PROGRAMMER'
print(nama[0:9])
print(nama.upper())
print(nama1.lower())
print(nama.capitalize())
print(nama.title())

uang = 271000000000000
print('{: ,}'.format(uang))
print('{: .2f}'.format(uang))
print('{: ,.2f}'.format(uang))

print(f'Rp.{uang:,}')
print(f'Rp.{uang:,.2f}')

penilaian = input('Masukan penilaian [Bagus/Tidak] : ').title()
print(penilaian)