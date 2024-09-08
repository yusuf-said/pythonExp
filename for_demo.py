sayilar = [1,3,5,7,9,12,19,21]
ucunkati = []
for i in sayilar:
    if i%3==0:
        print("ücün katı")
        ucunkati.append(i)
    else:
        print("üçe bölünmüyor")

print(ucunkati)

a=0

for num in sayilar:
    a = a + num
print(a)

for num_2 in sayilar:
    print(num_2**2)

