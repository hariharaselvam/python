#ex4
print "Problem no 4"
print "-----------------------------------------------------------"
print "The program to reverse each word of the given string"
string=raw_input("Enter a sring : ")
words=string.split()
print "The given input is "
print string
string=""
for w in words:
	w=w[::-1]
	string+=w+" "
print "The output string is"	
print string

print "-----------------------------------------------------------"

word2="".join(words)

print word2

word3="r a b b i d"
array=word3.split(" ")

print len(array),array

print "_".join(array)
