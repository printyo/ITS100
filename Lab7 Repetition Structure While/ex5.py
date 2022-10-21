while True:
  x = int(input("Enter an integer number:"))
  if 0 < x < 11:
    break
  else:
    print("1 - 10 !!!!")

output = ""
for i in range(1,x+1):
  output += str(i) + " "
  print(output)
if x == 10:
  output = output[:-2]
for i in range(1,x):
  output = output[:-2]
  print(output)