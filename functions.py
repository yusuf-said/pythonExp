def sayHello(name = "User"): #varsayılna olarak eklenir
    """sfsdfsdfs"""
    return "hello " + name

sayHello("yusuf")
sayHello("Ada")


msg = sayHello()
print(msg)
print(sayHello("aziz"))

def total(num1,num2):
    return num1 + num2

result = total(10,20)
print(result)

def yasHesaplama(dogumYili):
    return 2024 - dogumYili


def emekliligeKacYilKaldi(dogumYili_2, isim):
    yas = yasHesaplama(dogumYili_2)
    emeklilik = 65-yas
    if emeklilik>0:
        print(f"emeliliğinize {emeklilik} yıl kaldı")
    else:
        print("zaten emekli oldunuz")


emekliligeKacYilKaldi(1945,"yusuf")
print(help(sayHello))