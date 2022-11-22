myDict = {}

while True:
    x = input("Input: ")
    if x == "done":
        if len(myDict) == 0:
            print("Empty List")
            print("###Summary###")
        else:
            print("###Summary###")
            for i in myDict.items():
                print("Total Number of %s : %d"%(i[0],i[1]))
        break
    animal, n = x.split()
    n = int(n)
    if animal in myDict:
        myDict[animal] += n
    else:
        myDict[animal] = n
        