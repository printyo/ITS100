from math import *
def CirArea(x):
  print("The area of the circle is %.2f"%(pi*x*x))

def SqArea(x):
  print("The area of the square is %.2f"%(x*x))

x = float(input("Input a positive number: "))
if x <= 0:
  print("Wrong Input")
else:
  CirArea(x)
  SqArea(x)