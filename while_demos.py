# sayilar = [1,3,5,7,9,12,19,21]


# i=0
# while i<len(sayilar):
#     print(sayilar[i])
#     i=i+1 #sıfır vermezsen birtakım hatalar meydana gelir list index ile alakalı


# x =int(input("birinci sayı: "))
# y =int(input("ikinci sayı: "))

# i = x+1
# while i<y:
#     if i%2==1:
#         print(i)
#     else:
#         pass
#     i +=1



# a=100
# b=100
# c=1

# while a>0:
#     print(a)
#     a= a-1
a = []
for i in range (0,5):
    x = int(input("sayı girin: "))
    a.append(x)
print(a)

a.sort()
b=0
while b<5:
    print(a[b])
    b = b+1

