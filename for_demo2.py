sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]
besharfli=[]
for i in sehirler:
    lenght = len(i)
    if lenght<=5:
        print(i)
        besharfli.append(i)
    else:
        print("değildir")

print(besharfli)


urunler = [{"name":"samsung s6", "price":"3000"},
           {"name":"samsung s7", "price":"4000"},
           {"name":"samsung s8", "price":"5000"},
           {"name":"samsung s9", "price":"6000"},
           {"name":"samsung s10", "price":"7000"}]
a2=0

for urun in urunler:
    a = urun.get("price")
    a1= int(a)
    a2= a2 + a1
print(a2)

for prod in urunler:
    (a3) = int(prod.get("price"))
    if a3 <=5000:
        print(prod.get("name"))
    else:
        pass