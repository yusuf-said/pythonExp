#bir ifadeyi typeını değiştirmek için str() float() int() gibi komutlar kullanılır. type() verinin tipini görmemizi sağlar

#str to int
yazi1 = input("lütfen bir deger giriniz")

print(type(yazi1))

yazi1 = int(yazi1)
print(type(yazi1))


# int to float
yazi1 =float(yazi1)
print(type(yazi1))


# bool to int

dogru = True
print(type(dogru))
dogru = int(dogru)
print(type(dogru))