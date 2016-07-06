import pexpect
pro=pexpect.spawn("python getRandPrimes.py")
fout=open("randstaus.log","w")
pro.logfile_read=fout
pro.expect("number : ")
pro.send("10\n")
try:
	pro.expect(r"\b\d\b")
except pexpect.EOF:
	print "Eof happened"
except pexpect.TIMEOUT:
	print "Time out happened"
except Exception:
	print "Some error happened"
else:
	print "I got what I want :",pro.after
finally:
	pro.close(force=True)
print "I am done"
