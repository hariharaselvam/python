import re
print "Problem # 1 - regular expression"
print "The sum of numbers in a string"
s=raw_input("Enter a string with numbers ")
pat=raw_input("Enter the patten : ")
#pat=r"\b\d+\b"
list_of_numbers=re.findall(pat,s)
result=0
print list_of_numbers
for l in list_of_numbers:
	result=result+float(l)

print "The given string is",s
print "The list of numbers are",list_of_numbers
print "The sum of the numbers are:",result
