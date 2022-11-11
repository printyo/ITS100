import numpy as np

po1 = input("").split() #asks for input but it goes in as string
po2 = input("").split()
po3 = input("").split()

p1 = [int(po1[0]), int(po1[1]), int(po1[2])] #converts to integers
p2 = [int(po2[0]), int(po2[1]), int(po2[2])]
p3 = [int(po3[0]), int(po3[1]), int(po3[2])]

arr1 = np.array([p1,p2,p3]) #creates 2 array, so subtracting them gives 3 different answers
arr2 = np.array([p2,p3,p1])

dis = np.sqrt(np.sum((arr1-arr2)**2, axis=1)) #arr1-arr2 subtracts 3x3 - 3x3 leaving a 3x3 matrix. then squares the number in each matrix. then sums with axis =1 so you get 3 element in the matrix. then sqrts each element
print("The longest distance = %.2f"%(np.max(dis)))#outputs np.max(dis) largest number in the matrix