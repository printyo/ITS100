print("=================")
print("Cashier Program")
print("=================")
print()
i, sums = 0, 0
while True:
    x = input("Enter item price or -1 when finished: ")
    if x == "-1":
        break
    x = float(x)
    sums += x
    i += 1
print()
print("Total purchase amount is %.2f"%sums)
print()
pay = float(input("Your payment: "))
print()
print("You bought %d items today."%i)
print("Your change is %.2f baht"%(pay-sums))