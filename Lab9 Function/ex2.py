def LeftRotate(x,n):
  for i in range(n):
    z = x[0]
    del x[0]
    x.append(z)
  print("The left-rotated list:", x)

def RightRotate(x,n):
  for i in range(n*2):
    z = x[-1]
    del x[-1]
    x.insert(0,z)
  print("The right-rotated list:", x)

x = input("Enter 5 inputs: ").split()
try:
  rot = int(input("Enter an integer number of rotations (0-4): "))
except ValueError:
  print("Error!")
else:
  if 0 <= rot <= 4:
    LeftRotate(x, rot)
    RightRotate(x, rot)
  else:
    print("Error!")