odd = 0
even = 0
while True:
  x = int(input("Enter an integer (0 to exit) : "))
  if x == 0:
    print("----------------------------------")
    print("The number of even integers is", even)
    print("The number of odd integers is", odd)
    break
  elif x % 2 == 0:
    even += 1
  else:
    odd += 1