import re
str1="1 25 99 0 255 5 259 9 999"

#pattern='\s[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]\s'
pattern=r"\b[0-9]\b"
if re.search(pattern,str1):
	x=re.findall(pattern,str1)
	print x
else:
	print 'unmatched'
