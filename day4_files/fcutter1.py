.argv[2])
#infile=raw_input("Enter the file name: ")
fin=file(infile,"r")
fin.seek(0,2)
t=fin.tell()
#n=input()
p=t/n
fin.seek(0,0)
for i in range(n)