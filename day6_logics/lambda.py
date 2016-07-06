L=[1,2,3,4,5]

add = lambda x,y:x+y
sq=lambda x:x**2
L2=L[0:len(L)-2]
L3=L[1:len(L)-1]


L2=map(add,L[0:len(L)-2],L[1:len(L)-1])
print L2
L3=map(sq, L2)
print L3
s=sum(L3)
print s
