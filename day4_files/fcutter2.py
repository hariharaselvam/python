:
	data=fin.read(p)
	pat=str(i)+"."
	filename=re.sub(r"\.",pat,infile)
	fo=file(filename,"w")
	print filename
	fo.write(data)
	fo.close()
fin.close()