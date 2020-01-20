""" FOR LOOPS
-Used to iterate over a sequence (string,tupple,lists and dictionaries)
   for (variable name) in (sequence):
       body
-for loops can have an optional 'else'
"""
numbers=[1,2,3,4,5]
for i in numbers:
    if i%2 == 0:
     print(i,"is an even number")
    else:
        print(i,"is an odd number")
else:
    print("Last item has been reached")


#looping over a dictionary
