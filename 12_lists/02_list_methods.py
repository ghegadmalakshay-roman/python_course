marks=[5,2,21,5,7]
extramarks=[54,78,98]
print(marks)

marks.append(63) # this is will change original list

print(marks)

marks.pop() # removes last element
marks.extend(extramarks)
print(marks)