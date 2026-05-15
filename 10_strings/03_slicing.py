name = "Akshay012345678"

print(name[0:2]) # goes from 0 to 2-1(1) i.e 0 to 1 
print(name[2:-1]) # same as name[2:5] bcz -1 + size of string(6) which is 5

#print(name[0:10:n]) # skip n-1 characters
print(name[0:10:1]) # skip 0 characters as n is 1 now 
print(name[0:10:2]) # skip 1(2-1) characters as n is 2 now
print(name[0:10:3]) # skip 2(3-1) characters as n is 3 now

print(name[:4]) # will replace first empty number with 0 i.e same as name[0:4] 
print(name[1:]) # will replace second empty number with length i.e same as name[1:14]