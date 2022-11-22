p = 100

while True:
    x, y = input("Command: ").split()
    if x == "done" and y == "0":
        break
    if y.isnumeric() == False:
        print("Invalid command")
    else:
        y = int(y)
        if y < 1:
            print("Invalid command")
        elif x not in ["P","R"]:
            print("Invalid command")
        else:
            if x == "P":
                earn = y // 50
                print("You earned",earn,"points")
                p += earn
                print("Your accumulated points = %d points"%p)
            elif x == "R":
                if y > p:
                    print("Not enought points")
                else:
                    p -= y
                    print("You redeemed %d points"%y)
                    print("Your accumulated points = %d points"%p)