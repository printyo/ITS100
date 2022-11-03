from math import *

def CirArea(x):
    return pi*x*x
def SqArea(x):
    return x*x
try:
    x = float(input("Input a positive number: "))
except ValueError:
    print("Wrong Input")
else:
    if x <= 0:
        print("Wrong Input")
    else:
        print("The area of the circle is %.2f"%(CirArea(x)))
        print("The area of the square is %.2f"%(SqArea(x)))
        