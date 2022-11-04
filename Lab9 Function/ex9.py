from math import *

r = float(input("Enter the radius r of the cylinder: "))
h = float(input("Enter the height h of the cylinder: "))

def myCylinder(r,h):
  print("The volume is %.2f and the surface area is %.2f"%((pi*r*r*h),(2*pi*r*h+2*pi*r*r)))

myCylinder(r,h)