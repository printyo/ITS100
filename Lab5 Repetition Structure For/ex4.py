from math import *
num = int(input("Enter an integer number (n>0): "))
print("(1) Factorial of n (n!)")
print("(2) Summation of n integers")
choice = input("Select operation: ")
print("")
if num < 1:
  print("N/A Operation!")
else:
  if choice == "1":
    fac = factorial(num)
    print("Factorial of n (n!) = %d"%fac)
  elif choice == "2":
    sum = 0
    for i in range(1,num+1):
      sum += i
    print("Summation of n integers = %d"%sum)
  else:
    print("N/A Operation!")
