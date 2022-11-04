def SumOut():
  print("The summation is", sum(myList))

def MinOut():
  print("The minimum is", min(myList))

def MaxOut():
  print("The maximum is", max(myList))

myList = []
def UserInput():
  while True:
    x = input("Enter an input: ")
    if x == "Done":
      print()
      SumOut()
      MinOut()
      MaxOut()
      break
    else:
      try:
        x = int(x)
      except ValueError:
        print("Error")
        break
      else:
        if x < 0 :
          print("Error")
          break
        else:
          myList.append(x)

UserInput()