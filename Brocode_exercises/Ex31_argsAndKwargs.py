# Ex31__Args / kwargs

# *args = allows you to pass multiple non key arguments
# **kwargs = allows you to pass multiple keyword arguments
#           *unpacking operator

def invite(*args):
    for arg in args:
        print(arg)
print("Prakathish","you","great",sep="-")

def address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

address(state ="Tamilnadu",
        city="chennai",
        area="velachery")

# def shipping_label(**kwargs,*args): ------> wrong, first positional then keyword

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    for value in kwargs.values():
        print(value)

shipping_label("Mr.","Prakathish","Techie",
        state ="Tamilnadu",
        city="chennai",
        area="velachery")



