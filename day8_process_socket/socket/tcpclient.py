import socket
import sys,os
HOST='192.168.0.105'
PORT=5000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
	print " MENU "
	print "1.Testprime"
	print "2.Nextprime"
	print "3.Exit"
	ch=raw_input("Enter your choice : ")
	if ch=='3':
		s.sendall(ch)
		print "Bye"
		break
	if int(ch) < 1 or int(ch) >2:
		os.sysem('clear')
		print "Improper choice"
		continue
	n=raw_input("Enter a number : ")
	data=ch+":"+n
	s.sendall(data)
	result=s.recv(1024)
	os.sysem('clear')
	print "Result is : ",result
s.close()
