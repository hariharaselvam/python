import os,time
child=os.fork()
if child==0:
	print "Child started......"
	for i in range(10):
		print "Child : value of i = ",i
		time.sleep(1)
	print "Child is done......"
	os._exit(0)
os.wait()
for i in range(10):
	print "Parent: value of i = ",i
	time.sleep(1)
print "App is done"
os._exit(0)
