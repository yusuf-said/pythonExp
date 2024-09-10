bolenler = []
x = int(input("bölenlerinin bulunmasını istediğiniz sayıyı giriniz: "))

#asallık durumunun kontrol edilmesi

if x ==1:
    asallik = 12
else:
    for i in range(2,x):
        if x%i==0:
            asallik=False
            break
        else:
            asallik= True
print(asallik)


if asallik==False:
    for a in range(1,x+1):
        if x%a==0:
            bolenler.append(a)
            
        else:
            continue
elif asallik==True:
    bolenler.append[1,x]
elif asallik == 12:
    bolenler.append(1)

print(bolenler)