# def ChangeName(n):
#     n = "ahmet"

# name = "yusuf"
# ChangeName(name)
# print(name)



# list = [1,2,3,4,5]
# list_copy = [1,2,3,4,5]

# def Change(a_list):
#     a_list[0] = "str"

# Change(list)
# print(list)    #slicing

# Change(list_copy[:])
# print(list_copy

def add(*params):
    return sum(params) #for döngüsü ve istediğimiz kadar parametre eklememizi sağlıyor
print(add(2,1,2,3,4,5,67))



def displayUser(**args):
    print(type(args))

    for key,value in args.items():
        print(f" {key}  is  {value} ")
    print(key,value)

displayUser(name="yusuf", age =16, location="ist")

def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50, key1="value 1", key2="value2")
#tek yıldız liste içine alır, ** dictionary oluşturur ve her bilgi asterisk belli sıralama ile gider.