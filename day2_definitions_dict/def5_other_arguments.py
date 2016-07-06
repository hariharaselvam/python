
def sample(a,b,c):
	print a,b,c

def swap(a,b):
	return b,a

def samp1():
	print "1SAMP"

sample(10,20,300)
L=('abc','bca','cab')
sample(*L)
sample(L[0],L[1],L[2])
a=10
b=20
sample(a,b,0)
a,b=swap(a,b)
sample(a,b,0)

sample('a',"abc",0)
a_1="A1"
print a_1
x=10
y=30
print x,y
x,y=y,x
print x,y

z=swap(x,y)
print z

samp1()





