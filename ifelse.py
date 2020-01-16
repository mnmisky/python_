if 10+10==20:
    print ("my name")
else:
    print ("error") #body
 #marks=int(input("enter your marks"))  #bc input automatically makes them strings

password=input("Enter your password")
if len(password)<5:
     print("too short")
elif len(password)>15:
    print("too long")
elif len(password)>5 and len(password)<15:
    print("succesful")
