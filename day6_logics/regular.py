import re
s=raw_input("String : ")
p=raw_input("Pattern: ")
r=re.findall(p,s)
print r;
