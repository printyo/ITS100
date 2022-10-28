mydict = {}
x = input("Input a sentence: ").split()
for i in x:
  i = i.lower()
  if i in mydict:
    mydict[i] += 1
  else:
    mydict[i] = 1

print("Output:")
no = True
for key in mydict:
  if mydict[key] > 1:
    print(key)
    no = False

if no == True:
  print("none")