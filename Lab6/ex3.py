lis = []
for i in range(1,6):
  x = int(input("Input#%d: "%i))
  lis.append(x)
choice = input("Select the option: 1)Summary,2)average,3)min,4)max....")
if choice == "1":
  print("Your result is %d"%sum(lis))
elif choice == "2":
  print("Your result is %d"%(sum(lis)/5))
elif choice == "3":
  print("Your result is %d"%(min(lis)))
elif choice == "4":
  print("Your result is %d"%(max(lis)))