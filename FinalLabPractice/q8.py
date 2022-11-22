myDict = {}
while True:
    x = input("Input: ")
    if x == "done":
        print("----SUMMARY----")
        if len(myDict) == 0:
            print("The list is empty")
        else:
            for i in sorted(myDict.items()):
                print(i[0],i[1])
        break
    elif x.isnumeric():
        x = int(x)
        if 0 < x < 1001:
            if x in myDict.keys():
                myDict[x] += 1
            else:
                myDict[x] = 1
        else:
            print("ERROR")
    else:
        print("ERROR")
