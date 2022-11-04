from math import *

def SquareArea():
  x = float(input("Enter the lenght: "))
  print()
  print("The area of the square is %.2f"%(x*x))

def CircleArea():
  x = float(input("Enter the radius: "))
  print()
  print("The area of the circule is %.2f"%(pi*x*x))

choice = input("Do you want to find the area of a square (s) or a circle (c)?: ")
if choice == "s":
  SquareArea()
elif choice == "c":
  CircleArea()
else:
  print()
  print("Wrong Input")