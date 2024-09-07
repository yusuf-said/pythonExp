ogrenciler ={}

numbers = input("ögr no: ")
name = input("ögr adı: ")
surname = input("ögr soyad: ")
phone = input("pohne no: ")
ogrenciler[numbers]={
    "ad":name,
    "soyad":surname,
    "telefon": phone
}
numbers = input("ögr no: ")
name = input("ögr adı: ")
surname = input("ögr soyad: ")
phone = input("pohne no: ")
ogrenciler[numbers]={
    "ad":name,
    "soyad":surname,
    "telefon": phone
}
numbers = input("ögr no: ")
name = input("ögr adı: ")
surname = input("ögr soyad: ")
phone = input("pohne no: ")





ogrenciler[numbers]={
    "ad":name,
    "soyad":surname,
    "telefon": phone
}
print(ogrenciler)


print('*'*50)

ogrNo = input('öğrenci no: ')
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")

