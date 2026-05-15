# 0 1 1 2 3 5 8 13 fibonacci series

def fib(n):
    #Base case of recursion
    if(n==0 or n==1):
       return n
    return fib(n-2) + fib(n-1)

print(fib(9))      