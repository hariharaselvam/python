import re
def ipaddress(address):
	output=""
	upto255="[1]?\d{1,2}|[2][0-4]\d|[2][5][0-5]"
	pat=r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
	model=re.findall(pat,address)
	return model


s=raw_input("Enter an ip address : ")
ti=ipaddress(s)
print "The given ipaddress ",s," is ",ti
