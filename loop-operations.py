for item in range(2,10,2):
    print(item)

listt = list(range(0,100))
print(listt)



#enumerate

#lindex ve letter deperini verir.

greeting = "hello everbody"
index =0

for letter in greeting:
    print(f"index: {index} and letter {letter}")
    index = index + 1


for index_1,letter_1 in enumerate(greeting):
    print(f"index: {index_1} and letter {letter_1}")


#zip
list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]

for item in zip(list1,list2):
    print(item[0],item[1])


