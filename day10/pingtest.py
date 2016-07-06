import pexpect
import sys, time, os
if len(sys.argv)!=2:
	print "Wrong input!"
	sys.exit(1)
pro=pexpect.spawn('ping '+sys.argv[1])
try:
	pro.expect(r'icmp_seq=10')
	pro.sendcontrol('c')
except Exception:
	print "EOF"
	sys.exit(0)
pro.expect('\d+%')
r=pro.after
print r,"Packets loss"
