#range(1,101) #bc last no not included

for i in range(1,101):
    if (i%3 == 0) and (i%5==0) :
        print("FIZZBUZZ")
    elif i%3 == 0:
        print("FIZZ")
    elif i%5 == 0:
        print("BUZZ")
    else:
        print(i)
else:
    print("GAME ENDED")