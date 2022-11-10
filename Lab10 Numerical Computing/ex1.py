import numpy as np

x = int(input("Input size of matrix: "))

majorlst = []
minorlst = []
for row in range(1,x+1):
    for col in range(1,x+1):
        y = int(input("Input element at row %d column %d: "%(row,col)))
        minorlst.append(y)
    majorlst.append(minorlst)
    minorlst = []
    
print("\nOutput:\nMatrix =")
z = np.array(majorlst)
print(z)
print("Determinant = %.1f"%(np.linalg.det(z)))
print("Inverse Matrix =")
print(np.linalg.inv(z))