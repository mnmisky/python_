price=100
unit=int(input("Enter the number you units you wish to purchase"))
cost= price*unit
if cost <= 1000:
    print("YOUR TOTAL COST IS",cost)
else:
    discount=0.1*cost
    cost= 0.9*cost
    print("YOU HAVE BEEN AWARDED A 10% DISCOUNT EQUAL TO KSH,",discount)
    print("NEW AMOUNT PAYABLE IS KSH,",cost)