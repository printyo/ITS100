from math import *

d = float(input("Enter the distance to the building: "))
e = float(input("Enter the elevation angle in degree: "))

h = tan(radians(e))*d
print("The building height is %.4f." %h)