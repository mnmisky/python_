print("-------LOGIN TO FACEBOOK----")
username="Mark"
email="mark@gmail.com"
password="123456"

#prompting the user to enter their username
entered_username=input("Enter your username")

#crosschecking entred username with the one in "database"
if entered_username.lower() !=username:
    print("IVALID USERNAME.TRY AGAIN")
else: #if its all okay,can now prompt email address entry
    entered_email= input("Enter your email address")  

at_sign="@"
dotcom=".com"

#conditions for email 

if entered_email.lower() != entered_email: #check that the email is all lowercase
    print("EMAIL MUST BE LOWERCASE")
elif ((at_sign in entered_email) and (dotcom in entered_email)) == False: #if it has @ and .com
    print("INCORRECT EMAIL FORMAT")
elif entered_email!=email: #checking if it matches the database
        print("EMAIL DOES NOT MATCH")
else:
    entered_password=input("Enter your password") 

         

#crosschecking password
if password!=entered_password:
    print("Wrong password. Try again")
else:
        print("---LOGIN SUCCESSFULL---")
            
