mydict = {}
x = input("Input: ").split()
for i in x:
  i = i.lower()
  if i in mydict:
    mydict[i] += 1
  else:
    mydict[i] = 1
lists = sorted(mydict.values(), reverse=True)
maxNum = lists[0]
print("Output:")
for key, value in mydict.items():
  if value == maxNum:
    print(key, "=", value)