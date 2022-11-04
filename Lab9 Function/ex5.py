def SeatType():
  while True:
    x = input("Select the seat type (P or D or H): ")
    if x == "P" or x == "D" or x == "H":
      MovieType(x)
      break
    else:
      print("Wrong seat type! Please select again.")

def MovieType(seat):
  while True:
    x = input("Select the movie type (1 or 2): ")
    if x == "1" or x == "2":
      TicketPrice(seat, x)
      break
    else:
      print("Wrong movie type! Please select again.")

def TicketPrice(seat, movie):
  print()
  
  if movie == "1":
    if seat == "P":
      print("The tichket price is 100")
    elif seat == "D":
      print("The tichket price is 140")
    elif seat == "H":
      print("The tichket price is 400")
      
  elif movie == "2":
    if seat == "P":
      print("The tichket price is 150")
    elif seat == "D":
      print("The tichket price is 200")
    elif seat == "H":
      print("The tichket price is 500")

SeatType()