from math import *
def squareArea():
    x = float(input("Enter the length: "))
    print()
    print("The area of the square is %.2f"%(x*x))
    
def circleArea():
    x = float(input("Enter the radius: "))
    print()
    print("The area of the square is %.2f"%(pi*x*x))
    
x = input("Do you want to find the area of a square (s) or a circle (c): ")
if x == "s":
    squareArea()
elif x == "c":
    circleArea()
else:
    print()
    print("Wrong Input")