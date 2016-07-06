import pexpect,sys
pro=pexpect.spawn("sort")
fout=open("sortstaus.log","w")
pro.logfile_read=sys.stdout
Data=['Hello','hi','ok','fine','done']
for word in Data:
	pro.send(word+"\n")
pro.sendcontrol('d')
pro.expect(pexpect.EOF)
pro.close(force=True)
