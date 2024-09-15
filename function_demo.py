def writeFunc(yaz,adet):
    yaz = str(yaz)
    print(yaz*adet)
writeFunc(100,100)

def List_add(*args):
    liste=[]
    for arg in args:
        liste.append(arg)

print(List_add(1,2,43,3534,53,35,5353,345))


def tamBolen(sayi):
    tamBolenList = []
    for i in range(1,sayi+1):
        if sayi%i==0:
            tamBolenList.append(i)
        else:
            pass
    return tamBolenList

print(tamBolen(10000))
