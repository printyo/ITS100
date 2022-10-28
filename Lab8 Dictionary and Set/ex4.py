mydict = {}
while True:
  string = input("Input (DONE = exit): ")
  if string == "DONE":
    print("Output:")
    for i in sorted(mydict.values(),reverse=True):
      for j in mydict:
        if mydict[j] == i:
          print(j, i)
    break
  else:
    try:
      key, value = string.split()
      if key.isnumeric() and value.isnumeric():
        if int(key) > 0 and int(value) > 0:
          if key in mydict:
            print("Duplicated ID")
          else:
            mydict[key] = value
      else:
        print("Invalid input")
    except ValueError:
      print("Invalid input")