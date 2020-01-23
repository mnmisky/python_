"""
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that are sent to the function when it is called.

If the number of arguments is unknown, add a * before the parameter name
KEYWORD ARGUMENTS.
def my_function(child3, child2, child1):
      print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
"""
#Create a function that takes a name and returns a greeting.
def hello_name(name):
    print("hello",name)

hello_name("Gerald")

#Write a function that takes the base and height of a triangle and return its area.
def tri_area(base,height):
    return 0.5*(base*height)

#Create a function that finds the maximum range of a triangles third edge.
print(tri_area(3,2))

def next_edge(side_1,side_2):   
    print((side_1 +side_2)-1)

next_edge(9,2)

#Create a function that takes a list and returns the first element.
def get_first_value(list):
    return list [0]

print(get_first_value ([1,2,3]))
print(get_first_value ([80,5,100]))
print(get_first_value ([-500,0,50]))

#You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm. Return the total number of legs on your farm
def animals(chickens,cows,pigs):
    return (chickens*2) + (cows*4) +(pigs*4)

print (animals (2,3,5))
print (animals (1,2,3))
print (animals (5,2,8))

#Create a function that takes a list of numbers. Return the largest number in the list.
def findLargestNum(list):
    result=max(list)
    return result

print (findLargestNum([4, 5, 1, 3]))
print (findLargestNum([300,200,600,150]))
print (findLargestNum([1000,1001,857,1]))

#Given a list of integers, return the difference between the largest and smallest integers in the list.
def difference (list):
    dif= (max(list)) - (min(list))
    return dif

print (difference([10, 15, 20, 2, 10, 6]))
print(difference([-3, 4, -9, -1, -2, 15]))

#Create a function to concatenate two integer lists
def concat(list1,list2):
    return list1.extend(list2)

print (concat([1, 3, 5], [2, 6, 8]) )
print (concat([7, 8], [10, 9, 1, 1, 2]))
print (concat([4, 5, 1], [3, 3, 3, 3, 3]))

#Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
def comp (str1,str2):
    if (len(str1)) == (len(str2)):
        print ("True")
    else:
        print ("False")

comp("AB", "CD") 
comp("ABC", "DE")
comp("hello", "edabit")

#Write a function that converts a dictionary into a list, where each element represents a key-value pair
def convert_to_array (dict):
    list=[]
    for key,value in dict.items():
      list.append([key,value])
    return list
    
print (convert_to_array({ "a": 1, "b": 2 }))

#You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold.
def profit(dict):
    proft=(dict["sell_price"]- dict["cost_price"])*dict["inventory"]
    return round (proft)
print (profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}))


   
