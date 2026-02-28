# *args     = allows you to pass multiple non-keyword arguments  - tuples
# **kwargs  = allows you to pass multiple keyword arguments - Dictionary
#           *unpacking operator

def add(*args):
    print(type(args))
    total=0
    for arg in args:
        total+=arg
    return total

def address(**kwargs):
    print(type(kwargs))
    for key, values in kwargs.items():
        print(f"{key}  = {values}")
    print()

def displayName(*args):
    for arg in args:
        print(arg, end=" ")
    print()


def shippingLabel(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, values in kwargs.items():
        print(f"{key}  = {values}")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('apt')}  {kwargs.get('street')}  {kwargs.get('city')}")
    else:
        print(f" {kwargs.get('street')}  {kwargs.get('city')}")

    print()

print(add(1, 2, 3, 4, 5))

displayName("Sandeep", "Kumar", "Sharma")
displayName("Kavita", "Sharma")

address(street="160 Front Street", city="Toronto", state="Ontario", postCode="M8N 2L6")
address(apt="32", street="160 Front Street", city="Toronto", state="Ontario", postCode="M8N 2L6")

shippingLabel("Dr.", "Spongebob", "Squarepants", "III",
              street="160 Front Street",
              city="Toronto",
              state="Ontario",
              postCode="M8N 2L6")
shippingLabel("Mr.", "Spongebob", "Roundpants",
              street="160 Front Street",
              apt="32",
              city="Toronto",
              state="Ontario",
              postCode="M8N 2L6")


