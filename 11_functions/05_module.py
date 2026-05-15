#two types of module in python i.e internal or builtin modules and external modules
#Built in muodules : https://docs.python.org/3/py-modindex.html
import math
import os
import mymodule
import requests
print(math.sqrt(4))
# os.abort()
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)