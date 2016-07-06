import os
directory=raw_input("Enter a path      :  ")
filename= raw_input("Enter a file name :  ")
#extention=raw_input("Enter the file extention :")

fo=open(filename,"w")
print "---------------------------------------------------------------------------------------------------------------------"
list1=[x for x in os.walk(directory)]
list1=sorted(list1)
for l in list1:
	print l
for l in list1:
	for d in l:
		st=str(d)
		if st.find(".py")>0:
			print d
			fo.write(st)
			fo.write("\n")
		
print "The sub directories of {0} are stored in {1}".format(directory,filename)
fo.close
print "---------------------------------------------------------------------------------------------------------------------"

