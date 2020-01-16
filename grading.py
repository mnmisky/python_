math=int(input("Enter your math marks"))
eng=int(input("Enter your eng marks"))
swa=int(input("Enter your swa marks"))
sci=int(input("Enter your sci marks"))
sst=int(input("Enter your sst marks"))

if math>100 or eng>100 or swa>100 or sci>100 or sst>100 :
    print("SUBJECTS MARKS MUST BE LESS THAN 100")
else:
    print ("GENERATING YOUR REPORT")

total=math+eng+swa+sci+sst
average=total/5
print("Your Total is",total)
print("Your average is",average)
if average>=80 and average<=100:
    print("GRADE A")
elif average<79 and average>=70:
    print("GRADE B")
elif average>=60 and average<69:
    print("GRADE C")
elif average>=50 and average<59:
    print("GRADE D")
elif average<50 and average>0:
    print("PASS")
 
