z = 5 # global variable

def sum(a,b):
    c = a + b
    global z  #  please modify global z
    z = 7 # this will refer to global variable and will not create local variable
    return c

print(sum(3,5))
print(z)