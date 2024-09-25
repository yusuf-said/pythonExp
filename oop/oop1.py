
class calisan:
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad= soyad
        self.maas=2500
        self.eposta = self.ad+self.soyad+"@sirket.com"
    def tamad(self):
        return f"ad {self.ad} soyad {self.soyad}"

personel1 =calisan("ali","demir",2500) #içeriği kopyalar
# personel1.ad= "ali"
# personel1.soyad="demir"
# personel1.maas=2500

personel2= calisan("kerim","bakır",1950)
# personel2.ad="kerim"
# personel2.soyad="bakır"
# personel2.maas=1950

print(personel1.tamad())
print(personel2.ad,personel2.soyad,personel2.eposta)
print(personel1.ad,personel1.soyad)
print(calisan.tamad(personel1)) # fonk bu şekilde kullanilabilir
