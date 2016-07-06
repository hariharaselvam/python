import os
#address=raw_input("Enter the path : ")
#cmd="cd "+address
#os.system("cd /var/www")
#os.path="/var/www/";
#os.system("pwd")
for dirname, dirnames, filenames in os.walk("/var/www/"):
    # print path to all subdirectories first.
    #for subdirname in dirnames:
        #print os.path.join(dirname, subdirname)

    # print path to all filenames.
    for filename in filenames:
        print os.path.join(dirname, filename)
