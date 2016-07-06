import os
#os.system("ls -l")
fin=os.popen("ls -l")
for record in fin:
	print record
