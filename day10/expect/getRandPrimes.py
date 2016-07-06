import random
def testprime(m):
	if m < 2:return False
	for n in range(2,m):
		if m%n==0:return False
	return True

n=int(raw_input('Enter one number : '))
ranlist=[]
while len(ranlist)<n:
	num=random.randint(1,99)
	if testprime(num):
		ranlist.append(num)
print ranlist
