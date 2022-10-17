from math import *

x1 = float(input("Enter coordinate X for P1: "))
y1 = float(input("Enter coordinate Y for P1: "))
x2 = float(input("Enter coordinate X for P2: "))
y2 = float(input("Enter coordinate Y for P2: "))

d =(((x1-x2)**2)+((y1-y2)**2))**0.5
a = pi * (d/2)**2
c = pi*d
print("The length of the circle diameter is %.4f." %d)
print("The circle area and circumference are %.4f and %.4f." %(a,c))