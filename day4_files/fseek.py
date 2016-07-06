fin=file("temp.dat","r")



fin.seek(0,2)
t=fin.tell()
n=input()
p=t/n
fin.seek(0,0)
for i in range(n):
	data=fin.read(p)
	filename="my"+str(i)+".txt"
	fo=file(filename,"w")
	print data
	fo.write(data)
	fo.close()
fin.close()
