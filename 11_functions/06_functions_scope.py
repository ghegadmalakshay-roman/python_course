def sum(a,b):
    # a and b are local variables
    c =  a + b
    z = 1 # it creates local variable z and destroys after function is called
    return c


def greet():
    z = 32 # local variable
    print("Hello")


z=8  #z is global variables
print(z)
print(sum(3,6)) 
print(z)