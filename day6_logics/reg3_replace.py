import re
s=raw_input("Enter string ")
pat=raw_input("Enter the pattern ")
s1=re.sub(pat,'',s)
print s1
s2=re.subn(pat,'',s)
print s2
