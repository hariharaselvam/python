#Addition of two matrices

matrix1=[]


m1r=input("Enter the # of rows of matrix1 : ")
m1c=input("Enter the # of columns of matrix1 : ")

for i in range(m1r):
	ls=[]
	for j in range(m1c):
		nm=input("Enter elements ")
		ls.append(nm)
	matrix1.append(ls)


matrix2=[]
m2r=input("Enter the # of rows of matrix1 : ")
m2c=input("Enter the # of columns of matrix1 : ")


for i in range(m2r):
	ls=[]
	for j in range(m2c):
		nm=input("Enter elements ")
		ls.append(nm)
	matrix2.append(ls)

if m1r!=m2r or m1c!=m2c:
	print "Matrix addtion is not possible "
	exit(1)

matrix3=[]	
for i in range(m2r):
	ls=[]
	for j in range(m2c):
		nm=matrix1[i][j]+matrix2[i][j]
		ls.append(nm)
	matrix3.append(ls)

print "The first matrix is:"
for i in matrix1:
	row=""
	for j in i:
		row=row+str(j)+" "
	print row
print "The second matrx is:"
for i in matrix2:
	row=""
	for j in i:
		row=row+str(j)+" "
	print row
print "The third matrix is:"
for i in matrix3:
	row=""
	for j in i:
		row=row+str(j)+" "
	print row



		
