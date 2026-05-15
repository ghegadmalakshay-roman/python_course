# name="hello world" #strings are immutable
# # name[0]="R"  # You cannot modify string

# a=len(name)

# print(a)
# print(name.upper(),name)
# print(name.lower())
# print(name.capitalize())


# text= " Hello World "
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# text = "Python is fun and fun and fun"
# print(text.find("is"))
# print(text.replace("fun","awesome"))

# text = "Apples,Bananas,Orange"
# print(text.split(","))
# print(",".join(['Apples', 'Bananas', 'Orange']))#convert back to string values with comma seperate

text="Python123"
print(text.isalnum()) # checks if string is alpha numeric
print(text.isalpha())# checks if string is alphabet
print(text.isdigit())# checks if string is number
print(text.isspace())# checks if string is only space