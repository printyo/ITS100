n = 0
myList = []
main = True

while n <9:
    x = input("Input: ")
    if x in ["o","x"]:
        myList.append(x)
        n += 1
    else:
        print("Wrong input")
        main = False
        break

if main:
    print("-------")
    print("|%s|%s|%s|"%(myList[0],myList[1],myList[2]))
    print("-------")
    print("|%s|%s|%s|"%(myList[3],myList[4],myList[5]))
    print("-------")
    print("|%s|%s|%s|"%(myList[6],myList[7],myList[8]))
    print("-------")
    
