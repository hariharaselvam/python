import os
print "Hello world"
os.execvp("ls",["ls","-l"])
print "I am done"
