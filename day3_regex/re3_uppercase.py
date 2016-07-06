import re
print "Problem # 3 regular expression"
print "UPPER case words"
s=raw_input("Enter a string : ")
pat=raw_input("Enter the patten : ")
#pat=r"\b[A-Z]+\b"
uppers=re.findall(pat,s)
print "The words which are in UPPER case are:"
print uppers
