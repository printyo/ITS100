print("Welcome to Income Tax Computation Program")
income = int(input("Please enter your income (THB): "))
if income < 0:
  print("You are in debt!")
elif income < 15000:
  print("Tax expense = 0.00")
  print("Your net income after tax = %.2f"%income)
elif income < 50000:
  tax = (income - 15000) *0.05
  print("Tax expense = %.2f"%tax)
  print("Your net income after tax = %.2f"%(income-tax))
elif income < 100000:
  tax = 35000 *0.05 + (income - 50000)*0.075
  print("Tax expense = %.2f"%tax)
  print("Your net income after tax = %.2f"%(income-tax))
else:
  tax = 35000 *0.05 + 50000*0.075 + (income -100000)*0.1
  print("Tax expense = %.2f"%tax)
  print("Your net income after tax = %.2f"%(income-tax))