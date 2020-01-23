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