def ShowBMI(MyBMI):
  print("The user BMI is %.2f"%MyBMI)

def FindBMI(hh, ww):
  ShowBMI(ww/(hh*hh))

def UserInput():
  w = float(input("Input your weight (kilogram): "))
  h = float(input("Input your height (meter): "))
  FindBMI(h, w)

UserInput()