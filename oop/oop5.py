
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
    def __repr__(self):
        #string olmadıgını durumlarda
        return "__repr__ döndü"

    def __add__(self,other):
        return self.maas + other.maas
personel1 =calisan("ali","demir",2500) #içeriği kopyalar
personel2= calisan("kerim","bakır",1950)


print(int.__add__(5,9))
print(str.__add__("ali","veli"))


print(personel1 + personel2)


print(type(personel1))
print(personel2.__repr__())
#str() repr()









