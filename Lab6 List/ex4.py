namelist = ["Satawat", "Pisit", "Thanaphong", "Pished", "Nut", "Amon"]
program = True
while program:
  print("Student list:",namelist)
  de = input("Please enter a student name that you want to delete (q=exit): ")
  if de == "q":
    program = False
  else:
    print("You will remove '%s' from this class"%de)
    choice = input("Please type (Confor 'y' , Cancel 'n'): ")
    if choice == "y":
      namelist.remove(de)
    
      