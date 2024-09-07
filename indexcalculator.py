name = input("Adınız: ")
height = float(input("boyunuz: "))
weight = float(input("kilonuz: "))

formule = weight/(height*height)

print(formule)
if formule >=0 and formule <=18.4:
    print("zayıf")
elif formule >18.4 and formule<= 24.9:
    print("normal")
elif formule >24.9 and formule <=29.9:
    print("kilolu")
elif formule >29.9 and formule<=39.9:
    print("obez")
elif formule>=40:
    print("aşırı obez")
