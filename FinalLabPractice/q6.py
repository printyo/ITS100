global myDict
myDict = {}
def main():
    while True:
        sID, score = input("Enter student ID and score: ").split()
        if sID == "done" and score == "0":
            output()
            break
        elif sID.isnumeric() == False or len(sID) != 4:
            print("Invalid ID format!")
        elif int(score) < 0 or int(score) > 100:
            print("Invalid score!")
        else:
            if sID in myDict:
                print("The ID is already recorded!")
            else:
                myDict[sID] = score

def output():
    avg = 0
    print("List:")
    if len(myDict) == 0:
        print("> no score is recorded!")
    else:
        for x in sorted(myDict.keys()):
            for i in myDict.items():
                if i[0] == x:
                    print(i[0],i[1])
        for i in myDict.values():
            avg += int(i)
        avg /= len(myDict)
        print("There are %d student(s). The average score is %.2f points."%(len(myDict),avg))
            
            
main()