taskList = [23,"Jane",["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]

#checking for type of the variable
print(type(taskList))
print (type(23))

#print KES
tasklist=taskList[2]
print (tasklist[2])
print(tasklist[2]['currency'])


#print 560
print(tasklist[1])

#Use a function to determine the length of taksList
print(len(taskList))


#Change 987 to 789 without using an inbuilt -method or Assignment
x=taskList[3]
y=str (x) #this is called typecasting ie forcing something to be of another
z=y[::-1]
a= int(z)
taskList[3]=a
print (taskList)

#Change the name “John” to “Jane” .
#impossible because its a tupple hence immutable
