#ex6
print "Problem no 6"
print "------------------------------------------------------------"
print "Program to sum the numbers in the given string"
print ""
text=raw_input("Enter a string : ")
words=text.split()
sum=0
for w in words:
	if w.isdigit():
		sum+=int(w)
		

print sum
print "------------------------------------------------------------"
