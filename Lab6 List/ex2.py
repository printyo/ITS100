lis = input("Enter a comma-separated list: ").split(",")
oldList = []
for a in lis:
  for b in lis:
    for c in lis:
      if a != b:
        if b != c:
          if a !=c:
            newList = [a,b,c]
            if sorted(newList) not in oldList:
              print(a,b,c)
              oldList.append(newList)