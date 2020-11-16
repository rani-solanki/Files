places_list = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']
f=open("textfile.txt","w")
for i in places_list:
    f.write(i)
    f.write("\n")
f.close()