while True:
  print("===== MAIN MENU =====\n1. Addition\n2. Subtraction\n3.Exit")
  print()
  choice = input("Select an operation (1-3): ")
  if choice == "1":
    x,y = input("Enter two numbers: ").split()
    print("%s + %s = %d"%(x,y,(int(x)+int(y))))
  elif choice == "2":
    x,y = input("Enter two numbers: ").split()
    print("%s - %s = %d"%(x,y,(int(x)-int(y))))
  elif choice == "3":
    print("Bye!!!")
    break
  print("\n")