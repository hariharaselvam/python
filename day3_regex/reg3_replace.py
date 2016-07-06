import re
s="hello how are 12345 and 56789"
pat=raw_input("Enter the pattern ")
s1=re.sub(pat,'ABC',s)
print s1
s2=re.subn(pat,'abc',s)
print s2
