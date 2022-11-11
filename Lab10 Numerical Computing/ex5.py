import numpy as np

po1 = input("").split()
po2 = input("").split()
po3 = input("").split()

p1 = [int(po1[0]), int(po1[1]), int(po1[2])]
p2 = [int(po2[0]), int(po2[1]), int(po2[2])]
p3 = [int(po3[0]), int(po3[1]), int(po3[2])]

arr1 = np.array([p1,p2,p3])
arr2 = np.array([p2,p3,p1])

dis = np.sqrt(np.sum((arr1-arr2)**2, axis=1))
print("The longest distance = %.2f"%(np.max(dis)))