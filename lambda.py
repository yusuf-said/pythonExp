# def square(num): return num**2


numbers = [1,2,3,4,5,6]

# square2 = lambda num:num**2 #fonksiyon olabilir 
# result = list(map(square,numbers)) #map liste şeklinde elemanları fonksiyon içerisinde işlem gtörmesii sağlar. ya for döngüsü ya da list i,çerisine alınması gertekir


# for item in map(square,numbers):
#     print(item)

# result_2 = list(map(lambda num:num**2,numbers))
# print(square2(4))
# print(result,result_2)

# m = list(map(square2,numbers))
# print(m)


#filter function

numbers = [12,31,45,60,98,79]


def check(num):
    return num%2==0
#belirli şartları sağlaması ve ayıklasını filter ile yapılır
print(list(filter(check,numbers)))

check_num = lambda num:num%2==0

print(list(filter(check_num,numbers)))


fdshfkjshf = ["merhaba","selamlar"]
fsdhjkfsdhkjfskjdfhs=[]

sl = lambda letter:letter.upper()

fsdhjkfsdhkjfskjdfhs = list(map(sl,fdshfkjshf))
print(fsdhjkfsdhkjfskjdfhs)

