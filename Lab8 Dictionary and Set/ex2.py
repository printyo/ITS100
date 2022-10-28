x = input("Input: ").split()
mydict = {}
for i in x:
  if i.isnumeric():
    if i in mydict:
      mydict[i] += 1
    else:
      mydict[i] = 1

good = True
for key, value in mydict.items():
  if good == False:
    break
  if key == str(value):
    good = True
  else:
    good = False



if good == True:
  print("Output: good sequence")
else:
  print("Output: not good sequence")