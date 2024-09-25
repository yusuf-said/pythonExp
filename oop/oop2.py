
class calisan:

    zam_orani =1.05
    per_say = 0
    kackerecalisti =0
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad= soyad
        self.maas=maas
        self.eposta = self.ad+self.soyad+"@sirket.com"
        self.per_say +=1
        calisan.kackerecalisti+=1
        print(f"kaç kere çalıştı {calisan.kackerecalisti}")
    def tamad(self):
        return f"ad {self.ad} soyad {self.soyad}"
    def artir(self):
        self.maas = (self.maas*self.zam_orani)

personel1 =calisan("ali","demir",2500) #içeriği kopyalar
print(calisan.per_say)
print(personel1.per_say,"w")
personel2= calisan("kerim","bakır",1950)
print(personel2.per_say,"a")



print(personel1.maas)
personel1.artir()
print(personel1.maas)
print(calisan.per_say)
personel2.zam_orani=1.1
print(personel2.maas)
personel2.artir()
print(personel2.maas)
print(calisan.per_say)






