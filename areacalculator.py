import math


print("Hello! Please pick to you want to calculate area.")

print("1 for Triangle \n 2 for Rectangle \n 3 for square \n 4 for circle \n 5 for Quit the app.")
pick = int(input("Please select one: "))

if pick==1:
    height =int(input("please input the height: "))
    base = int(input("please input the base: "))
    area = (base*height)/2
    print(f"area of triangle is {area}")
elif pick==2:
    lenght= int(input("please input the lenght: "))
    width = int(input("please input the widht: "))
    area = lenght*width
    print(f"area of rectangle is {area}")

elif pick==3:
    side = int(input("please input side: "))
    area = side**2
    print(f"area of square is {area}")
elif pick == 4:
    pi = math.pi
    radius = int(input("please input the radius: "))
    area = pi*(radius**2)
    print(f"area of circle is {area:.0f}")
else:
    print("error: selected wrong key, try again")


