import re
print "Problem # 4 regular expression"
print "1-255 of given strings"
s=raw_input("Enter a string : ")
pat=raw_input("Enter the pattern : ")
result=re.findall(pat,s)
print " numbers between 1-255 in string "
print result

