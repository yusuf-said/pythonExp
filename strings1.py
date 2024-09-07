name = "yusuf"
surname = "çöpcü"
age = 30


info = ("My name is " + name + " " +surname+"."+ " I am " + str(age) + " old.")

# print(info[0:10])

# print(len(info))

# print(info[0:7])

#formatting

print("my name is {} {} i am {} years old.".format(name,surname,age))
print(f"my name is {name} {surname} i am {age} old")

result = 291/500
print("result is {r:1.1000}".format(r=result))