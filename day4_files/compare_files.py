first_file="urls.txt"
second_file="compare.txt"

def get_urls(file_name):
    fin=file(file_name,"r")
    list= fin.readlines()
    fin.close()
    return list


first_list= get_urls(first_file)
second_list = get_urls(second_file)
output={}
for url in first_list:
    count=second_list.count(url)
    if count>0:
        output[url]=count
        print "url     : "+url
        print "count   : "+str(count)
        print ""



