import sys
import re
if len(sys.argv)!=3:
	print "I need 2 arguments as one filename and an integer"
	exit(1)
if not sys.argv[2].isdigit():
	print "I need the 2nd argument as an integer"
	exit(1)
linecount=0;
fin=file(sys.argv[1],"r")
while True:
	line=fin.readline()
	if len(line)==0: break;
	linecount=linecount+1
fin.close()

filecount=int(sys.argv[2])

lof=linecount/filecount

print "total # lines",linecount
print "total # files",filecount
print "minimum lines",lof

filename=sys.argv[1]

filelist=[]

fo=[]
for i in range(filecount):
	pat=str(i+1)+"."
	newfile=re.sub(r"\.",pat,filename)
	print newfile
	filelist.append(newfile)
	fo.append("1")
	fo[i]=file(newfile,"w")
fin=file(filename,"r")


cf=0
i=0
rang=len(filelist)-1
while True:
	line=fin.readline()
	if len(line)==0:break
	cf=cf+1
	fo[i].write(line)
	if cf==lof:
		cf=0
		if i<rang:
			fo[i].close()
			i=i+1
		
	
fo[rang].close()
fin.close()
	
	
	
	


	
