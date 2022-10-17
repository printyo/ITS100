for i in range(5):
  x = int(input("enter a number between 1 and 20: "))
  if x > 20 or x < 1:
    print("number is invalid")
  else:
    if x % 2 == 0:
      print("%d is an even number"%x)
    else:
      print("%d is an odd number"%x)