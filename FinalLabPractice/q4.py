from operator import itemgetter
myList = []
while True:
    run = True
    z = input("Input: ")
    if z == "done":
        break
    x, y = z.split()
    if y.isnumeric() == False:
        print("Invalid input")
    else:
        y = int(y)
        if y < 0 :
            print("Invalid input")
        else:
            for i in range(len(myList)):
                if x == myList[i][0]:
                    print("Duplicated player")
                    run = False
            if run:
                myList.append([x,y])

if len(myList) == 0:
    print("No players")
else:
    avg = 0
    sortList = sorted(myList, reverse=True, key=itemgetter(1))
    for i in range(len(sortList)):
        avg += sortList[i][1]
    avg /= len(sortList)
    for i in range(len(sortList)):
        if i == 0:
            print("%s\t%d\tGold"%(sortList[i][0],sortList[i][1]))
        elif sortList[i][1] > avg:
            print("%s\t%d\tSilver"%(sortList[i][0],sortList[i][1]))
        else:
            print("%s\t%d"%(sortList[i][0],sortList[i][1]))