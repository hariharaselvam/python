import pexpect
import sys
m = pexpect.spawn('python mail.py')
m.logfile_read = sys.stdout
m.expect("Username:")
m.sendline("")
m.expect("Password:")
m.sendline("")
m.expect("To address :")
m.sendline("hbalasubramanian@asmltd.com")
m.expect("Subject :")
m.sendline("test")
m.expect("Enter the content. Your last line should be as 'end'")
m.sendline("hello")
m.sendline("end")
m.expect("test has been send to hbalasubramanian@asmltd.com")
m.close()