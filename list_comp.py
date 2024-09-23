numbers=[x**2 if x%2==0 else "bölünmüyor"  for x in range(10) if x%3==0]

for i in numbers:
    print(i)


string = "güzel günler"

letter = [l for l in string]
print(letter)


years = [1990,2020, 1976,1986]
age = [2019-y for y in years if 2019>=y]
print(age)



numbers_1 = [(a,b)  for a in range(3) for b in range(3) if b%2==0]
print(numbers_1)