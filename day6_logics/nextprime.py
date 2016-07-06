def isprime(num):
	for i in range(2,num):
		if num % i ==0:
			return False
	return True

def nextprime(num):
	num=num+1
	while isprime(num)!= True:
		num=num+1
	return num

number=input("Enter a number : ")
if isprime(number):
	print "The number ",number," is a prime"
else:
	print "The number ",number," is not a prime"

next=nextprime(number)
print "The next prime number of " ,number," is ",next
