money = int(input("Enter money you have: "))
price = int(input("Enter price of item: "))
tax = price*0.08
total = price + tax
print("Tax: %d"%tax)
print("Total price : %d"%total)
if money >= total:
  print("yes you have enough money to buy")
else:
  print("You have shortfall of %d, you cannot buy."%(total-money))