import re


b = re.compile(r"\d+\.\d*")
print(b.match("10.1"))