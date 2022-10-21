lis = []
while True:
  x = input("Enter a name:")
  if x == "exit":
    print(lis)
    break
  else:
    lis.append(x.capitalize())