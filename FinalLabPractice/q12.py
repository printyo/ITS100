myDict = {"1":0,"2":0,"5":0,"10":0}
total = 0
print("Welcome to coin deposit machne")
while True:
    x = input("Please inset coin: ")
    if x == "done":
        print("<-----Deposit Summary----->")
        print("1 baht coins ->",myDict["1"])
        print("2 baht coins ->",myDict["2"])
        print("5 baht coins ->",myDict["5"])
        print("10 baht coins ->",myDict["10"])
        print("Deposit Amount: %d baht"%total)
        break
    if x.isnumeric():
        if x in myDict:
            myDict[x] += 1
            x = int(x)
            total += x
            print("You inserted %d baht coin"%x)
            print("Current Balance: %d baht"%total)
        else:
            print("Only 1,2,5 and 10 baht coin are allowed")
    else:
        print("Invalid Input")