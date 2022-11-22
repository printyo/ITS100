from operator import itemgetter
global myList
myList = []
def main():
    while True:
        append = True
        z = input("Enter student name and score: ")
        if z == "end":
            output()
            break
        x, y = z.split()
        y = int(y)
        for i in range(len(myList)):
                if x == myList[i][0]:
                    print("Duplicate name!")
                    append = False
        if x == "end":
            output()
            break
        elif y < 0 or y > 100:
            print("Invalid score!")
        elif append == True:   
            myList.append([x,y])

def output():
    print("List:")
    if len(myList) == 0:
        print("> empty list!")
    else:
        revList = sorted(myList, reverse=True, key=itemgetter(1))
        for i in range(len(revList)):
            print(revList[i][0],"\t",revList[i][1])
    
main()