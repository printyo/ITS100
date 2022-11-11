import numpy as np

smallList = []
bigList = []
for i in range(12):
  c = int(input(""))
  smallList.append(c) #keeps appending into list
  if len(smallList) == 4: #once number of element in list reaches 4 append to the main list and clears the old
    bigList.append(smallList)
    smallList = []

array = np.array(bigList) 
left = array[:,0:3] #takes left 3x3 matrix
right = array[:,3] #takes the total into 1x3 matrix
right = np.reshape(right,(3,1)) #converts into 3x1 matrix
xyz = np.matmul((np.linalg.inv(left)),right) #look at the lecture slides, xyz = inv(mat1)(mat2)

print("Solution:") #Output
print("x = %.2f"%(xyz[0]))
print("y = %.2f"%(xyz[1]))
print("z = %.2f"%(xyz[2]))