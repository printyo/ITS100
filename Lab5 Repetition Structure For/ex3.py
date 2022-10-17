print("Multiplication table:")
num = input("Please enter a number between 1 to 25: ")
count = 1
if num.isnumeric() == False:
  print("You entered invalid number")
else:
  num = int(num)
  if num < 1 or num > 25:
    print("You entered invalid number")
  else:
    print("Multiplication table of %d :"%num)
    for i in range(12):
      print("%d x %d = %d"%(num,count,num*count))
      count += 1