first = int(input("Enter the first number: "))
upper = int(input("Enter the upper bound: "))
step = int(input("Enter the step: "))

def myRange(FirstVal, UpperBound, StepSize):
  print("Range =", [*range(FirstVal, UpperBound, StepSize)])

myRange(first,upper,step)