a={3,2,1,4}
b={4,5,6,1}

c=a.union(b) # returns a new set that is the union of a and b
#print(c)

d=a.intersection(b) # returns a new set that is the intersection of a and b and
# containes only the elements that are present in both sets
print(d)

e=a.difference(b) # returns a new set that contains elements in a but not in b
print(e)