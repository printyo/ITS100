import numpy as np

bigList = []
smallList = []

for i in range(1,13):
    x = int(input("Input C%d: "%i))
    smallList.append(x) #add to minor list
    if len(smallList) == 4: #when theres 4 element in the list, append to big list and clear
        bigList.append(smallList)
        smallList = []

mat = np.array(bigList) #convert to matrix
mat1 = mat[0:3,0:3] #takes 3x3 matrix from 3x4
mat2 = mat[:,3] #takes the last column 3x1
mat2 = np.reshape(mat2,(3,1)) #converts horizontal array to vertical
try:
    xyz = np.matmul(np.linalg.inv(mat1),mat2)
    print("\nSolution:")
    print("x = %.2f"%xyz[0])
    print("y = %.2f"%xyz[1])
    print("z = %.2f"%xyz[2])
except: #if cant find inverse
    print("\nUnable to find solution")