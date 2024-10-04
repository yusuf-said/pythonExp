#decarator tekrar tanımlar ve güncelleme secenegi sunar fonk en son güncel haline cevirir
class calisan():
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad= soyad
    @property #parametre olarak cekebilmek için değişken gibi
    def eposta(self):
        self.email = self.ad+self.soyad+"@sirket.com"
        return self.email
    @property
    def tamad(self):
        return f"ad {self.ad} soyad {self.soyad}"

    @tamad.setter
    def tamad(self,gelen_isim):
        ad,soyad= gelen_isim.split(" ")
        self.ad = ad
        self.soyad=soyad


    @tamad.deleter
    def tamad(self):
        self.ad = None
        self.soyad = None
        print("kullanıcı bilgileri silindi")


personel1 =calisan("ali","demir") #içeriği kopyalar

personel1.tamad ="Can Sultan"


print(personel1.ad)
print(personel1.eposta)
print(personel1.tamad)

del personel1.tamad







