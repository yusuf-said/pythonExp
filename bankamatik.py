Ahesap ={
    "ad":"a kişisi",
    "hesapNo": "42489274",
    "hesap": 2000,
    "ekHesap":350}
access=""

Bhesap ={
    "ad":"B kişisi",
    "hesapNo": "42489290",
    "hesap": 21000,
    "ekHesap":12350}



Chesap ={
    "ad":"c kişisi",
    "hesapNo": "42489252",
    "hesap": 1000,
    "ekHesap":1035}

account=input("hesap no giriniz")
print(Ahesap.get("hesapNo",))
if account==Ahesap.get("hesapNo"):
    access = Ahesap
elif account==Bhesap.get("hesapNo"):
    access= Bhesap
elif account==Chesap.get("hesapNo"):
    access= Chesap
else:
    print("yanlış giriş yaptınız tekrar deneyin")

print(f"hoşgeldiniz", access.get("ad"))

def paracek(access):
    total= access.get("hesap")+ access.get("ekHesap")

    x= input("lütfen çekmek istediğiniz miktarı giriniz.")
    x = int(x)
    if access.get("hesap")>=x:
    
        total-=x

        print("para çekme işlemi başarıyla gerçekleşmiştir. Kalan bakiye(ek hesap dahil )",str(total))
    else:
        if total>=x:
            print("ek hesap kullanılsın mı? [E/H]")
            a = input("E/H")
    
            if a=="E":
                total-=x
                print("para çekme işlemi başarıyla gerçekleşmiştir. Kalan bakiye(ek hesap dahil)", str(total))
            elif a=="H":
                print("hesabınızdan çıkılıyor")
            else:
                print("hatalı giriş. lütfen yeniden deneyiniz.")
        else:
            print("yetersiz bakiye")



    

paracek(access=access)
