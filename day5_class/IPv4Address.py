import re
class IPv4Address:
	def __init__(self,ipadd):
		self.ipadd=ipadd
	def isvalid(self):
		
		pat1=r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
		pat2=r"\b[1]?\d{1,2}\b|\b[2][0-4]\d\b|\b[2][5][0-5]\b"
		dotted=re.findall(pat1,self.ipadd)
		count=re.findall(pat2,dotted[0])
		if len(count)==4:
			return True
		else:
			return False

	
ipadd=raw_input("Enter an ip address : ")
ip=IPv4Address(ipadd)
if ip.isvalid():
	print "The given ipaddress ",ipadd," is valid"
else:
	print "The given ipaddress ",ipadd," is invalid"


