import re
s="75d0h33m"
pat="\d+[a-z]"
result=re.findall(pat,s)
print result
