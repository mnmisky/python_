classes_held=int(input("Enter the total number of classes held"))
classes_att=int(input("How many classes did you attend?"))

percentage= (classes_att/classes_held)*100
print ("Your attendance percentage is",percentage)
if percentage>100:
    print("IMPOSSIBLE!!!.YOU CANT HAVE ATTENDED MORE CLASSES THAN WERE HELD")
elif percentage >75 :
    print("YOU ARE ALLOWED TO DO THE EXAM")
else:
    print("YOUR ATTENDANCE IS TOO LOW")
    medical="y"
    response=input("DO YOU HAVE A MEDICAL CAUSE?. REPLY 'y' or 'n'")
    response=response.lower()
    if response==medical:
        print("YOU ARE ALLOWED TO SIT THE EXAM ")
    else:
            print("YOU ARE NOT ALLOWED TO SIT THE EXAM")
