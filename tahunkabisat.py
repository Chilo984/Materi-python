def kabisat(tahun):
    if tahun % 400 == 0:
        return True
    if tahun % 100 == 0:
        return False
    if tahun % 4 == 0:
        return True
    else:
        return False
    
tahun = int(input('masukan tahun :'))
print("")


if kabisat(tahun):
    print(tahun,"adalah tahun kabisat")
else:
    print(tahun,"bukan tahun kabisat")