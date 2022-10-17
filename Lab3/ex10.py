from math import *
paint = float(input("Input the covered area for one paint bottle (cm square): "))
n = int(input("Input the number of the spheres: "))
r= float(input("Input the radius of each sphere (cm): "))

sa = 4*pi*r**2
paint_need = ceil((sa*n)/paint)
print("The paint bottles are needed to paint the surface of spheres is %d."%paint_need)