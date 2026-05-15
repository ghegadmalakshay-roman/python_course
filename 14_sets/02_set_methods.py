s={3,23,45,67,2}

print(s)

s.add(32)
s.add(322)

print(s)

s.remove(2)

print(s)
#s.remove(55) # will raise an error if 55 is not present in the set
s.discard(55) # will remove 55 if it is present, but will not raise an error if it is not present