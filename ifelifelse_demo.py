# name = input("isminiz:")
# age = int(input("yaşınız: "))

# if age>=18:
    
#     grad = input("eğitim durumu \n üniveriste mezunu iseniz 1'e \n ilkokul iseniz 2'ye \n lise mezunu iseniz 3'e basın: ")
#     if grad == "1" or grad=="3":
#         print("ehliyet almaya uuygunsunuz.")
#     else:
#         print("ehliyet almaya uygun değilsiniz")
# else:
#     print("ehliyet almaya uygun değilsiniz")

# ########################333333

x = input("ilk notunuz: ")
y = input("ikinci notunuz: ")
x = int(x)
y = int(y)
ort = (x+y)/2
ort = float(ort)
print(ort)


if ort<=24 and ort>=0:
    print("0")
elif ort>=25 and 44>=ort:
    print("1")
elif ort>=45 and ort<=54:
    print("2")
elif ort>=55 and ort<=69:
    print("3")
elif ort>= 70 and ort<=84:
    print(4)
