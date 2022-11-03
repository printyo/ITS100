
def showBMI():
    print("The user BMI is %.2f"%myBMI)
    
def findBMI(hh, ww):
    global myBMI
    myBMI = ww/(hh*hh)
    
def userInput():
    x = float(input("Input your weight (kilogram): "))
    y = float(input("Input your height (meter): "))
    findBMI(y,x)
    showBMI()
    
userInput()