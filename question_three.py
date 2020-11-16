banks_list=["kotak","hdfc","rbl","sbi","bank of india"]
banks=open("question3.txt","w")
for i in banks_list:
    banks.write(i)
    banks.write("\n")
banks.close()