name = "global str"


def greeting():
    name = "local str"
    def hello():
        name = "local 2 str"
        print("hello", name)
    hello()

greeting()


###################

x=50

def test():
    global x
    print(x)
    x=100
    print(x)

test()
#global eklenince her şey oldugu gibi değişir.
print(x)

