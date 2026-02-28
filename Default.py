import time

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount)  * ( 1+ tax )


print(net_price(500,0.1,0.05))
print(net_price(500))
print(net_price(500))
print(net_price(500))



def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

#count(5)
#count(30, 15)

def hello(greeting, title, firstname, lastname):
    print(f"{greeting} {title} {firstname} {lastname}")

hello(greeting="Hello", title="Mr.", firstname="SpongeBob", lastname="Squarepants")

hello(lastname="Squarepants", greeting="Hello", title="Mr.", firstname="SpongeBob")

hello("Hello",lastname="Squarepants", title="Mr.", firstname="SpongeBob")