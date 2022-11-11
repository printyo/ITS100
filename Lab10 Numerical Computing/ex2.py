import numpy as np

smallList = []
bigList = []
for i in range(12):
  c = int(input(""))
  smallList.append(c)
  if len(smallList) == 4:
    bigList.append(smallList)
    smallList = []

array = np.array(bigList)
left = array[:,0:3]
right = array[:,3]
right = np.reshape(right,(3,1))
xyz = np.matmul((np.linalg.inv(left)),right)

print("Solution:")
print("x = %.2f"%(xyz[0]))
print("y = %.2f"%(xyz[1]))
print("z = %.2f"%(xyz[2]))