
class calisan:

    zam_orani =1.05
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad= soyad
        self.maas=maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
    def tamad(self):
        return f"ad {self.ad} soyad {self.soyad}"
    def artir(self):
        self.maas = (self.maas*self.zam_orani)

    @classmethod
    def zam_orani_degis(cls,yeni_oran):
        cls.zam_orani = yeni_oran
    @classmethod
    def yenipersonel(cls,pbilgisi):
        ad,soyad,maas = pbilgisi.split("-")
        return cls(ad,soyad,maas)
    @staticmethod
    def tel_no(telefon):
        return telefon.split(" ")

personel1 =calisan("ali","demir",2500) #içeriği kopyalar
personel2= calisan("kerim","bakır",1950)

mpersonel1="veli-can-4000"
mpersonel2 = "mert-haydar-3200"
ypersonel2= calisan.yenipersonel(mpersonel2)
ad, soyad, maas =mpersonel1.split("-")
print(ad,soyad,maas)
ypersonel1 = calisan(ad,soyad,maas)

print(ypersonel2.eposta)

gtelefon ="0123 456 78 90"
print(calisan.tel_no(gtelefon))









