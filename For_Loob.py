colors = ['merah','kuning','hijau']
numbers = [1,3,4,5]
desc = 'Aku Pintar'

for color in colors:
    print(color)
for des in desc:
    print(des)
for i in range(5):
    print(i)
for index, color in enumerate(colors):
    print(index,color)
for number,color in zip(numbers,colors):
    print(number,color)

data = {'nama':'DION SENOWIJAYA','nim':23090073}

for datas in data:
    print(datas)
for value in data.values():
    print(value)
for label,value in data.items():
    print (label,"i",value)
for i in range(10):
    if i % 2 == 0:
        print(i,'bilangan Genap')
    else:
        print(i,'bilangan Ganjil')