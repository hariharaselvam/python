import sys
count=len(sys.argv)
if count < 3:
	print "I need atleast 2 file names"
	exit(1)
destination=sys.argv[count-1]
fout=file(destination,"w")
for i in range(1,count-1):
	fin=file(sys.argv[i],"r")
	
	fout.write(sys.argv[i])
	fout.write("\n")
	while True:
		line=fin.readline()
		if len(line)==0:break
		
		fout.write(line)
	
	fout.write("-----------------------------------")
	fout.write("\n")
	fin.close()
fout.close()
print ""
print "The contents of ",sys.argv[1:count-1],"are copied to ",destination,"file"


