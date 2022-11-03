from math import *

def myCylinder(r,h):
    print("The volume is %.2f and the surface area is %.2f"%(pi*r*r*h,(2*pi*r*h+2*pi*r*r)))
    
x = float(input("Enter the radius r of the cylinder: "))
y = float(input("Enter the height h of the cylinder: "))
myCylinder(x,y)