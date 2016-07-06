import re
s="hello how 4470 and 4483 are done"
pat=raw_input("Enter the pattern : ")
if re.search(pat,s):
	print "Found"
else:
	print "Not found"
