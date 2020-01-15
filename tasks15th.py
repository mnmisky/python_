#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function

a=[5,10,15,20,25]
#show max value
print (max(a))
#show first and last element (either use .append or step)
print (a[::4])

#With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half values in one line and the last half values in one line.
numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first= numbers[0:4]
last=numbers[5:]
#print on multiple lines
print (first)
print(last)
#get rid of brackets in tupple to strings
fstring= str(first)
lstring= str(last)
#remove first and last character in string (replace, strip)
print (fstring.strip("()"))
print (lstring.strip("()"))
