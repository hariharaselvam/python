#ex2
print "Problem no 2"
print "-------------------------------------------------------------"
print "Program to generate prime numbers"
n=int(raw_input(" Enter the number of prims : "));

list=[];

num=2;
while len(list) < n:
	
	for i in range(2,num):
		if num % i == 0:
			break;
	else:
		list.append(num)
		

	num+=1
print "The list first %d prime numbers are :"%n	
print list
print "-------------------------------------------------------------"
