class Person:
    
    # class attributes
    address ="3" #her objeyi etkiler

    #constructor (yapıcı metod)
    def __init__(self, name, year):             
        
    # object attr
        self.name = name
        self.address2 = ""
        self.years = year
        print("init metodu çalıştı")

    #methods

#object,instance
p1 = Person("yusuf",1998)
p1.address2="19823719837"
p2 = Person("aziz", 1990)
print(p1.address2)
print(p2.address2)

print(p1.address,p2.name)
print(type(p1),type(p2))
#print(p1 == p2) false