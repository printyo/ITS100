x = int(input("Enter the first number: "))
y = int(input("Enter the upper bound: "))
z = int(input("Enter the step: "))

def myRange(firstVal, upperBound, stepSize):
    print("Range =", [*range(firstVal,upperBound,stepSize)])
    
myRange(x,y,z)