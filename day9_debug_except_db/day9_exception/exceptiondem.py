#exception

L=[10,20,30,40,50]

try:
	x=int(raw_input('Enter a number : '))
	y=int(raw_input('Enter a number : '))
	z=x/y
	print "z= ",z
	print L[20]
except ValueError:
	print "I got value error"
except IndexError:
	print "I got Index error"
except ZeroDivisionError:
	print "I got zero division error"
except Exception:
	print "I got someother error"
else:
	print "No exception occured"
finally:
	print "I do always"
print "Application ends here"
