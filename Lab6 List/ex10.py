fruit = input("List of fruits: ").split(",")
for i in fruit:
  if len(i) > 5:
    print("%s is 6 characters or more!"%i)
  else:
    print("%s is only %d long!"%(i,len(i)))