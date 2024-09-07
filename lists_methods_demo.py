names = ["ali","yagmur","hakan","deniz"]
years= [1998,2000,1998,1987]

names.append("cenk")
names.insert(0,"sena")
#names.remove("deniz")
print(names.index("deniz"))
print(names)
# deneme = names.index("hjksadfdsha")
# print(deneme)
result = "ali" in names
print(result)

names.reverse()
print(names)
names.sort()
print(names)

years.sort()
print(years)

r = years.count(1998)

print(r)

