
class calisan():

    zam_orani =2.00
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad= soyad
        self.maas=maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
    def tamad(self):
        return f"ad: {self.ad} soyad: {self.soyad}"
    def artir(self):
        self.maas = (self.maas*self.zam_orani)

class gelistirici(calisan):
    def __init__(self,ad,soyad,maas,p_dili):
    #diğerkiler önceden gelmişti.
        calisan.__init__(self,ad,soyad,maas) #super()
        #super.__init(#parametreler yine girilir)
        self.p_dili=p_dili
        self.zam_orani= 1.2






personel1 =calisan("ali","demir",2500) #içeriği kopyalar
personel2= calisan("kerim","bakır",1950)

gel1 = gelistirici("adem","çakır",1500,"Python")
print(gel1.p_dili,gel1.tamad(),gel1.maas)
gel1.artir()
print(gel1.maas)

class Yonetici(calisan):
    def __init__(self,ad,soyad,maas,calisanlar=None):
        calisan.__init__(self,ad,soyad,maas)
        if calisanlar is None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar
    def eleman_ekle(self,eleman):
        self.calisanlar.append(eleman)
    def eleman_cikar(self,eleman):
        self.calisanlar.remove(eleman)
    def calisan_listeler(self):
        for eleman in self.calisanlar:
            print(eleman.tamad())



yon1 = Yonetici("pelin","su",1200,[gel1,personel1,personel2,gel1])
yon1.eleman_cikar(gel1)
yon1.eleman_ekle(personel1)
print(yon1.calisan_listeler())



print(isinstance(yon1,Yonetici)) #nesnenin sınıfa ait olmadıgını kontrol eder.

print(issubclass(Yonetici,calisan)) #sınıfın alt sınıf olup olmadıgını kontrol eder.
