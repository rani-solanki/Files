user=input("enter the num")
lis=list(user)
i=0
a=1
pl=[]
while(i<len(lis)):
    pl.append(lis[-a])
    i=i+1
    a=a+1
print(pl)