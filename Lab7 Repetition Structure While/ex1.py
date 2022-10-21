lis = []
while True:
  x = input("Enter a word:")
  if x == "exit":
    print(lis)
    break
  elif x[-1] == "y":
    x = x[:-1]
    x += "ily"
    lis.append(x)
  else:
    lis.append(x)