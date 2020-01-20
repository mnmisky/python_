sample=['aba','xyz','abc','1221']
count=0
for i in sample:
    if len(i) > 2:
        if (i.startswith(sample[0]) != i.endswith(sample[-1])):
            count=count+1
            
print(count)
