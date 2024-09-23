class Person:
    
    # class attributes
    address ="" #her objeyi etkiler

    #constructor (yapıcı metod)
    def __init__(self, name, year):             
        
    # object attr
        self.name = name
        self.address2 = ""
        self.years = year
        print("init metodu çalıştı")
    
    #methods
    #object methods
    def intro(self):
        print(f"hello there. my name is {self.name}")
    def calculateAge(self):
        return 2024 - self.years
#object,instance
p1 = Person("yusuf",1998)
p1.address2="19823719837"
p2 = Person("aziz", 1990)
print(p1.address2)
print(f"my name is {p1.name} and my age is {p1.calculateAge()}")

print(p1.address,p2.name)
print(type(p1),type(p2))
#print(p1 == p2) false


class Circle:
    #class object attributes
    pi = 3.14

    def __init__(self,yaricap=1):
        self.yaricap =yaricap

    def cevre_hesap(self):
        return self.yaricap*2*self.pi
    
    def alan_hesaplama(self):
        return (self.yaricap**2)*self.pi
    

c1 = Circle(12)

print(f"alan {c1.alan_hesaplama()} ve cevrem {c1.cevre_hesap()}")