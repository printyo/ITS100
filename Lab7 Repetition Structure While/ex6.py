while True:
    print("===== MAIN MENU =====")
    print("1. Addition\n2. Subtraction\n3. Exit")
    print()
    choice = input("Select an operation (1-3): ")
    if choice == "1":
        x,y = input("Enter two numbers: ").split()
        x = int(x)
        y = int(y)
        print("%d + %d = %d"%(x,y,(x+y)))
        print()
        print()
    elif choice == "2":
        x,y = input("Enter two numbers: ").split()
        x = int(x)
        y = int(y)
        print("%d - %d = %d"%(x,y,(x-y)))
        print()
        print()
    elif choice == "3":
        print("Bye!!!")
        break