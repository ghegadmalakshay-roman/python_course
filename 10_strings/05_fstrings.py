#string formatting

template = "Dear {} , How are You. Take this {}$ bag"
a="John"
a1=10000
b="Jack"
b1=2000
c="Marrie"
c1=3000

s1=template.format(a,a1)
print(s1)

print(f"{b} you are good and take this {b1}$ bags")