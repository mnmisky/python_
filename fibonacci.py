""" 
Method 1: when using 'steps' eg. print the first 20 fibonacci numbers
"""
# def fibo(n):
#     x=0
#     y=1
#     mylist=[0,1]
#     if n==0:
#      print(x)
#     elif n==1:
#         print(y)
#     else:
#         for i in range (2,n):
#             z=x+y
#             mylist.append(z)
#             print(mylist)
#             x=y
#             y=z
            
# print(fibo(10)) 
"""
Method 2: when given range eg. print fibonacci numbers from 0 to 50
"""
x=0
y=1
z=x+y
mylist=[0]
for i in range (0,50):
    if z<50:
     
     mylist.append(z)
     z=x+y
     x=y
     y=z

print(mylist)