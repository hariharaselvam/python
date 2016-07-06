import re,sys
try:
	filename=raw_input("Enter a file name : ")
	fin=file(filename,"r")
	lines=fin.readlines()
	fin.close()
except IOError:
	print "File not found!"
	sys.exit(0)

while True:
	find=raw_input("Enter the word to search : ")
	Li=[]
        i=0
	for line in lines:
		i=i+1
		if re.search(find,line):
			Li.append(i)

	if len(Li)==0:
		print "Search not found for ",find," in ",filename
	else:
		for l in Li:
			print l, " : ",lines[l-1]

	cont=raw_input("Do you want to continue?(y/n)")
	if cont=="n":break
		

