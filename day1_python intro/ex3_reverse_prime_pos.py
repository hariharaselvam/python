#ex3
list=['Hariharaselvam','Madurai','Bangalore','Chennai','Hydrabad','NewDelhi','Bombay', 'Truvandrum','Mysore','Truchi','Coimbatore','New york','Athense','Parris','Melborn','Singapore']
print "----------------------------------------------"
print "The list before reversing the prime positions"

order=0
for l in list:
	print order,"=>",l
	order+=1

size=len(list)
print ""
print "The size of the list is ",size
print ""

primes=[];

num=2;
while  num < size:
	
	for i in range(2,num):
		if num % i == 0:
			break;
	else:
		primes.append(num)
		

	num+=1

print "The prime positions of the given list"
print primes
print ""
half=len(primes)/2

j=0;
k=-1;
while j < half:
	
	temp=list[primes[j]]
	list[primes[j]]=list[primes[k]];
	list[primes[k]]=temp;
	j+=1
	k+=-1
	
order=0
print ""
print "The list after reversing the prime positions"
for l in list:
	print order,"=>",l
	order+=1

print "----------------------------------------------"
