#key value
#belli bir koda belli bir değer gelir

# sehirler = ["kocaeli","istanbul"]
# palakalar = 41,34 


# print(sehirler[palakalar.index(41)])


# plakalar = {"istanbul" : 34, 41 : "kocaeli"} 
# print(plakalar[41])

# plakalar["ankara"] = 6
# print(plakalar["ankara"])

users ={
    "ahmet çınar":{
    "roles":["admin","moderator"],
    "age": "28",
    "address": "esenler",
    "phone": "+905905353458"
    },
    "mehmet kaya":{
        "roles":["user"],
        "age": "21",
        "address": "bagcılar",
        "phone": "+9043255453"
    }
}
print(users["ahmet çınar"]["roles"][0])