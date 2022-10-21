x = int(input("Enter an integer number:"))
for row in range(1,x+1):
  for col in range(1,x+1):
    if row == 1 or row == x or col == 1 or col == x:
      print("o", end=" ")
    elif col >= row:
      print("x", end=" ")
    else:
      print(" ", end=" ")
  print()