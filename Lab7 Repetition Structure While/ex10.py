while True:
  x = input("Enter an integer ('X' to exit): ")
  if x == "X":
    break
  else:
    try:
      x = int(x)
      for row in range(1,x+1):
        for col in range(1,x+1):
          if row == col or col == (x+1-row):
            print("X", end=" ")
          else:
            print(".", end=" ")
        print()
    except ValueError:
      print()