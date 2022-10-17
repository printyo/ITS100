x = input("Input: ")
num = 0
fail = False
start = "|"
for i in x:
  if i not in "XO.":
    fail = True
  num += 1
if num != 9 or fail:
  print("Error")
else:
  print("-------")
  for i in x[:3]:
    start += i +"|"
  print(start)
  start = "|"
  print("-------")
  for i in x[3:6]:
    start += i +"|"
  print(start)
  print("-------")
  start = "|"
  for i in x[6:]:
    start += i +"|"
  print(start)
  print("-------")
    