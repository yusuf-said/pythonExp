message = "merhaba arkadaşlar"

m_1 = message.join("**")

print(m_1) #basına ve sonuna karakter ekler.

m_2 = message.replace("m", "M")
print(m_2) #string ifadeden karakter değitirmeyi sağlar.

m_3 = message.title() #ayrık olanları büyük harfle yazar.
print(m_3)

message_1 = " merhaba arkadaşlar"
m2_4 = message_1.strip()
print(m2_4) #boşlukları siler.

m_4 = message.split("a")
print(m_4) #kümelere ayırır.

m_5, m_6 = message.lstrip("merhaba"), message.rstrip("arkadaşlar") #sağdan ve soldan siler.

print(m_5,m_6)
message_2 = "merhaba merhaba arkadaşlar arkadaşlar"
m_7 = message_2.strip(" mr")
print(m_7)

m_8 = message_2.replace(" ","-",1)
print(m_8)