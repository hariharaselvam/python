import re
s="Hello how 1234567 and 56789 are done"
pat=raw_input("Enter the pattern : ")

result=re.findall(pat,s)
print result
