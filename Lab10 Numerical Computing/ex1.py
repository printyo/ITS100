import numpy as np

x = int(input(""))

smallList = []
bigList = []

for row in range(1,x+1):
  for col in range(1,x+1):
    el = int(input(""))
    smallList.append(el)
  bigList.append(smallList)
  smallList = []

array = np.array(bigList)

print("Output:")
print(array)
print("Determinant =  %.1f"%(np.linalg.det(array)))
print("Inverse matrix = ")
print(np.linalg.inv(array))