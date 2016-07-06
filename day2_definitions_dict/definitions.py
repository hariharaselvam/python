def prime(num):
	for i in range(2,num):
		if num % i == 0:
			return False
	return True

def testprime(m):
	if m < 2:return False
	for n in range(2,m):
		if m%n==0:return False
	return True
	
def nextprime(num,count=1):
	i=0
	primes=[]
	while i < count:
		num=num+1
		while testprime(num)!=True:
			num=num+1
		i=i+1
		primes.append(num)
	if count==1:
		return num
	return primes

def getprimes(lower,upper):
	primes=[]
	num=lower
	while num < upper:
		while testprime(num)!=True:
			num=num+1
		primes.append(num)
		num=num+1
	return primes


number=int(raw_input("Enter a number : "))
if testprime(number):
	numtype="Prime"
else:
	numtype="Not Prime"
print "The given number {0} is  {1}".format(number,numtype)

next=nextprime(number)

print "The next prime number of {0} is {1}".format(number,next)

count=int(raw_input("Enter the number of next primes : "))
primelist=nextprime(next,count)

print "The next {0} prime number(s) after {1} is :".format(count,next)
print primelist
print ""
lower=int(raw_input("Enter the lower bound : "))
upper=int(raw_input("Enter the upper bound : "))

primelist2=getprimes(lower,upper)
print "The list of prime numbers between {0} and {1} are :".format(lower,upper)
print primelist2

