list1 = input("List 1: ").split(",")
list2 = input("List 2: ").split(",")
newList = []
for a in list1:
  for b in list2:
    if a == b:
      if int(a) in newList:
        continue
      else:
        b = int(b)
        newList.append(b)
print(newList)

#1,1,2,3,5,8,13,21,34,55,89
#1,2,3,4,5,6,7,8,9,10,11,12,13

#1,2,5,7,7,8,9,10,13,13,21,24,24
#1,2,7,9,9,9,13,24