import re
print "Problem # 2 - regular expression"
print "Atleast one vowels in a word"
s=raw_input("Enter a string : ")
#pat=raw_input("Enter the patten : ")
pat="\w*[aeiouAEIOU]\w*"

words=re.findall(pat,s)
print "The list of words having atleast one vowels"
print words
