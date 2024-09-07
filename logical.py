x = 5 
hak = 0
devam = "e"
# result = 5 < x <10
# print(result)

#and #her iki tartafın dogru olması lazım
result = x<=10 and x>=5
d = hak>0 and devam == "e"
print(d)

#or  #ikisiden birisinin doğru olması gerekir  dogru dogru dogru  false false false
result_2 = x>0 or x%2==0
print(result_2)
#not
result_3 = not(x<0)
print(result_3)
print(result)
