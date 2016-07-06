class ShortMsgError(Exception):
	def __init__(self,msg):
		self.error=msg
	def whathappened(self):
		return "ShortMsgError:"+self.error

print "Message starts here"
try:
	message=raw_input("Enter some message(minimum 10 bytes): ")
	if len(message) < 10 :
		raise ShortMsgError("Message is too short to handle")
	print "Process the message : "+message
except ValueError:
	print "I got Value Error "
except IndexError:
	print "I got Index error"
except ZeroDivisionError:
	print "I got zero division error"
except ShortMsgError,e:
	print e.whathappened()
except Exception:
	print "I got someother error"
else:
	print "No exception occured"
finally:
	print "I do always"
print "Application ends here"
