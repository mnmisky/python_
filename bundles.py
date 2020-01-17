account_balance=300
spend= int (input("How much do you want to spend"))

if spend > account_balance:
    print("insufficient funds")
elif spend>0 and spend <50:
  print("SUCCESSFULLY PURCHASED 200 MBS ")
  account_balance=account_balance-spend
  print ("YOUR NEW BALANCE IS",account_balance)
elif spend>=50 and spend<100:
    print("SUCCESSFULLY PURCHASED 500 MBS")
    account_balance=account_balance-spend
    print("YOUR NEW BALANCE IS",account_balance)
else:
    pass
