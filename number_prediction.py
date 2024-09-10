import random 
hak = int(input("sayı giriniz"))
puan = 100
sayac = 0
number = random.randint(1,100)
print(number)
while hak>0:
    hak-=1
    sayac+=1
    x = int(input())
    if x==number:
        print(f"doğru bildiniz {sayac}.seferinizde dogru bildiniz puanınız:{100 - (100/(hak+1))}")
        break
    elif number> x:
        print("aşağı")
    else:
        print("yukarı")
    if hak==0:
        print(f"hakkınız bitt sayi: {number}")