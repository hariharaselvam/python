import urllib2
sock=urllib2.urlopen("http://www.google.com")
html=sock.read()
sock.close()
print html
