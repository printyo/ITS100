try:
  x = int(input("Input 12-digit string: "))
  x = str(x)
except ValueError:
  print("invalid input")
else:
  if len(x) != 12:
    print("invalid input")
  else:
    s = int(x[0]) + int(x[1])*3 + int(x[2]) + int(x[3])*3 + int(x[4]) + int(x[5])*3 + int(x[6]) + int(x[7])*3 + int(x[8]) + int(x[9])*3 + int(x[10]) + int(x[11])*3
    t = 10 - (s%10)
    if t == 10:
      c = 0
    else:
      c = t
    print("Output: check digit = %d"%c)