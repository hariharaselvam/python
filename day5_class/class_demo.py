class Rectangle:
	count=0
	def __init__(self,x=0,y=0):
		self.length=x
		self.width=y
		Rectangle.count=Rectangle.count+1
	def __str__(self):
		return "Rectangle({0},{1})".format(self.length,self.width)

	def area(self):
		return self.length* self.width

	def __add__(self,other):
		return Rectangle(self.length+other.length,self.length+other.width)
	def __eq__(self,other):
		return self.length==other.length and self.width==other.width
	def isSquare(self):
		return self.length==self.width

	def scale(self,length=0,width=0):
		if self.length+length>0:
			self.length=self.length+length
		if self.width+width>0:
			self.width=self.width+width
		
			
			
		
	@staticmethod
	def getcount():
		return Rectangle.count

R1=Rectangle(2,4)
print R1
a=R1.area()
print "Area=",a


R2=Rectangle(2,4)
print R2
b=R2.area()
print "Area=",b

R3=R1+R2
print R3
c=R3.area()
print "Area=",c

co=Rectangle.getcount()
print "count=",co

if R1==R2:
	print "Same"
else:
	print "Not same"

if R1.isSquare():
	print "square"

R1.scale(3,4)
print R1



