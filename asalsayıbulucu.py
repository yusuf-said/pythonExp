x = int(input("sayı giriniz: "))



if x==1:
    print("asal sayı değildir")
for i in range(2,x):
    if x%i==0:
        print("asal sayı değildir")
        break
    elif i==(x-1):
        print("asal sayıdır")
        
    