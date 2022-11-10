import numpy as np

p1 = input("Input coordinate of P1: ").split()
p2 = input("Input coordinate of P2: ").split()
p3 = input("Input coordinate of P3: ").split()

one = np.array([int(p1[0]), int(p1[1]), int(p1[2])]) #convert into matrix and change to integers
two = np.array([int(p2[0]), int(p2[1]), int(p2[2])])
three = np.array([int(p3[0]), int(p3[1]), int(p3[2])])

oneTwo = (np.sum((one-two)**2))**0.5 #use the given formula
twoThree = (np.sum((two-three)**2))**0.5
oneThree = (np.sum((one-three)**2))**0.5

print("Output:")
x = [oneTwo, twoThree, oneThree]
print("The longest distance = %.2f"%(max(x)))