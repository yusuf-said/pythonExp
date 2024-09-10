name = "yusf said"

for letter  in name:
    if letter == "i":
        continue
    else:
        print(letter)


x=0
while x<5:
    x+=1

    if x==2:
        continue
    else:
        print(x)

x=0
result=0
while x<=100:
    x= x+1

    if x %2==0:
        continue
    result+=x

print(x,result)


