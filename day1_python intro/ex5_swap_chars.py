#ex 5
print ""
print "Problem no 5"
print "------------------------------------------------------------"
print "The program to swap first an last charecters of each word in a given string"
text=raw_input("Enter a sring : ")
print "The given string is"
print text
words=text.split()
text=""
for w in words:
	
	pos=len(w)-1
        text =text+w[-1]+w[1:pos]+w[0]+" "
print "The resulted string is"
print text
print "------------------------------------------------------------"

