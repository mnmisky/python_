#anything wrapped in single/double quotes
number="10"
name="Misky"
drink='coke'

#getting a character from a string- ie. string indexing
x=name[0] #from left to right
print(x)
z=name[2]
print(z)
print(name[2])
#sliced=course[-4] #from right to left

#String slicing- getting a range of characters 
course="programming"
sliced=course[3:7]
sliced=course[3:] #all remaining 
sliced=course[-8:-4] #when its negative, its the other way round
sliced=course[-4:-8] #wrong
print(sliced)
#when you slice, when it ends is not included
#string is immutable- you cant change a string once you declare it
str1="Mwai"
str2="Kibaki"
fullname= str1 + " " + str2 #concatenation
print(fullname)
print (str1.lower())


