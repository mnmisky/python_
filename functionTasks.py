#Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No". 
yez=input("enter your response:")
if yez == "Yes" or  yez=="yes" or yez=="YES":
    print ("Yes")
else:
    print("No")

#Implement a function that takes as input three variables, and returns the largest of the three
one=int (input("Enter your first number:"))
two=int (input("Enter your second number"))
three=int (input("Enter your third number"))

if one > two and one>three :
    print (one,"is the largest number")
elif two>one and two>three :
    print (two,"is the largest number")
else:
    print (three,"is the largest number")

#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list


