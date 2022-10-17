x = input("Enter a single letter: ")
if x in "ABC":
  print("The digit 2 corresponds to the letter %s on the telephone."%x)
elif x in "DEF":
  print("The digit 3 corresponds to the letter %s on the telephone."%x)
elif x in "GHI":
  print("The digit 4 corresponds to the letter %s on the telephone."%x)
elif x in "JKL":
  print("The digit 5 corresponds to the letter %s on the telephone."%x)
elif x in "MNO":
  print("The digit 6 corresponds to the letter %s on the telephone."%x)
elif x in "PRS":
  print("The digit 7 corresponds to the letter %s on the telephone."%x)
elif x in "TUV":
  print("The digit 8 corresponds to the letter %s on the telephone."%x)
elif x in "WXY":
  print("The digit 9 corresponds to the letter %s on the telephone."%x)
else:
  print("There is no digit on the telephone that corresponds to %s."%x)