print("========Welcome to Hi!! Car Wash========")
choice = input("Choose your services: W=Wash C=Wash+Vacuum >>> ").lower()
if choice == "w":
  size = input('Enter your car size: "S", "M", "L" : ').lower()
  if size == "s":
      print("Price = 100 Baht")
  elif size == "m":
      print("Price = 120 Baht")
  elif size == "l":
      print("Price = 140 Baht")
  else:
      print("You Enter the wrong car size")
elif choice == "c":
  size = input('Enter your car size: "S", "M", "L" : ').lower()
  if size == "s":
      print("Price = 120 Baht")
  elif size == "m":
      print("Price = 140 Baht")
  elif size == "l":
      print("Price = 160 Baht")
  else:
      print("You Enter the wrong car size")
else:
  print("Please Choose Your Services")