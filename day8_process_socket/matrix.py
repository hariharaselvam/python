import random,time
n=int(raw_input("Enter the order of n : "))
Mat=[]
for i in range(n):
	row=[]
	for j in range(n):
		row.append(0)
	Mat.append(row)
matrix=""


i=0
cells=n*n
#c1=time.time()
while i<cells:
	x=random.randint(0,n-1)
	y=random.randint(0,n-1)
	value=random.randint(1,99)
	if Mat[x][y]==0:
		Mat[x][y]=value
		i=i+1
	
#c2=time.time()
#c3=c2-c1
for m in Mat:
	print m
#print "Starting time:",c1
#print "Ending time :",c2
#print "Difference :",c3
print "Elapsed time:",time.clock()
