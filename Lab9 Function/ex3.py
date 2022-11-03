lis = []

def sumOut():
    print("The summation is",sum(lis))
def minOut():
    print("The minimum is", min(lis))
def maxOut():
    print("The maximum is", max(lis))

def userInput():
    while True:
        x = input("Enter an input: ")
        if x == "DONE":
            print()
            sumOut()
            minOut()
            maxOut()
            break
        else:
            try:
                x = int(x)
            except ValueError:
                print("Error!")
                break
            else:
                if x < 0:
                    print("Error!")
                    break
                else:
                    lis.append(x)
                
userInput()
