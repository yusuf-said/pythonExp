site = "yusufsaid.com.tr"
greeting = "merhaba python kursuna hoşgeldiniz"


print(site[10:13])


length = len(greeting)
rr = length-11
print(length,rr)
print(greeting[rr:length])
print(greeting[-15:-1]) # left to right value is not important
print(greeting[::-1]) #reverse

# change to "Hello world" w to W

rrr = "Hello world"
s = rrr[0:5]
changed = s + "W" + rrr[6:]
print(changed)