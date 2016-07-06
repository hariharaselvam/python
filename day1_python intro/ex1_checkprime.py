#ex 1
#Prim number or not

num=int(raw_input("Enter a number : "))

for i in range(2,num):
	if num % i == 0:
		print "%d is not prime" % num
		break;
else:
	print "%d is a prime number" % num

