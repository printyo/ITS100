import numpy as np

x = int(input("")) #input size of matrix

smallList = []
bigList = []

for row in range(1,x+1):
  for col in range(1,x+1):
    el = int(input(""))
    smallList.append(el) #append into the same row
  bigList.append(smallList) # once row finishes append to the main list
  smallList = [] # and clears the smaller list ready for next loop

array = np.array(bigList) #convert into matrix

print("Output:")
print(array)
print("Determinant =  %.1f"%(np.linalg.det(array))) #command to find determinant and string format inside
print("Inverse matrix = ")
print(np.linalg.inv(array)) #command to find inverse