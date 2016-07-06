#Variable of arguments
def sample(*t):
	print t

def add(*t):
	print t
	su=0
	for e in t:
		su=su+e;
	return su

sample()
sample(10,20,30)
sample('Hariharaselvam',4470,('Madurai','Chennai','Bangalore'))
print add(1,2,3,4,5)
print add(10,-30,10.6)
