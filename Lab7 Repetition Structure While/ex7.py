print("===================")
print("Cashier Program")
print("===================")
print()
summ,count = 0, 0
while True:
  x = input("Enter item price or -1 when finished: ")
  if x == "-1":
    print("\nTotal purchase amount is %.2f\n"%summ)
    pay = float(input("Your payment: "))
    print("\nYou bought %d items today.\nYour change is %.2f baht."%(count,(pay-summ)))
    break
  else:
    count += 1
    summ += float(x)
    