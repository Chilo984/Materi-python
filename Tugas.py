def hitung_kuota_kredit(pendanaan):
    kuota_kredit = pendanaan * 0.8
    return kuota_kredit

pendanaan = int(input("Masukkan pendanaan: "))
kuota_kredit = hitung_kuota_kredit(pendanaan)

if kuota_kredit > 5000000:
    print("Maaf, kuota kredit anda melebihi batas.")
else:
    print("Kuota kredit yang diperlukan adalah Rp.", kuota_kredit)