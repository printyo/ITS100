num = input("enter no. of lines: ")
print("")
if num.isnumeric():
  num = int(num)
  if num > 0:
    for i in range(1,num+1):
      if i % 2 != 0:
        print("-"*i)
      else:
        print("*"*i)
  else:
    print("Error")
else:
  print("Error")