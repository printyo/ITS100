from math import *

d = float(input("Enter the sphere diameter: "))
r = d/2
v = (4/3)*pi*r**3
sa = 4*pi*r**2
print("The length of the sphere radius is %.4f."%r)
print("The sphere volume and the surface area are %.4f and %.4f."%(v,sa))