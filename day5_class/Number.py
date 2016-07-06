class Number:
	

	def __init__(self,number):
		self.number=number
	
	def __str__(self):
		return "Number ({0})".format(self.number)
	
	
	

	def testprime(self,num=0):
		if num==0:
			num=self.number
		if num<2:
			return False
		for i in range(2,num):
			if num%i==0:
				return False
		return True 


	def nextprimes(self,count=1):
		i=0
		primes=[]
		num=self.number
		while i < count:
			num=num+1
			while self.testprime(num)!=True:
				num=num+1
			i=i+1
			primes.append(num)
		if count==1:
			return num
		return primes

	def iseven(self):
		return self.number%2==0

	def pefsquare(self):
		num=self.number
		for i in range(1,num):
			ans=i
			if (num/i) == ans:
				return True
		return False
		

		
		
	
num=int(raw_input("Enter a number : "))
n=Number(num)
print n
if n.testprime():
	print num," is a prime"
else:
	print num," is not a prime"
if n.iseven():
	print num," is an even"
else:
	print num," is not an even"

if n.pefsquare():
	print num," is a perfect square"
else:
	print num," is not a perfect square"

b=n.nextprimes()
print num," next prime is ",b
c=int(raw_input("Enter the count : "))
ln=n.nextprimes(c)
print ln



