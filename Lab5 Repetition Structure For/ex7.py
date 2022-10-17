count = 0
l = 0
s= 0
h=0
for i in range(10):
  x = input('Feeling Like ("L"), Sad ("S"), and Heart("H")? ')
  if x == "L":
    l += 1
    count+=1
  elif x == "S":
    s += 1
    count+=1
  elif x == "H":
    h += 1
    count+=1
  else:
    print("Invalid input, accepts only (L/S/H).")
print("============")
print("Total is %d"%count)
print("============")
print("Like: %d (%.2f%%)"%(l, (l/count)*100))
print("Sad: %d (%.2f%%)"%(s, (s/count)*100))
print("Heart: %d (%.2f%%)"%(h, (h/count)*100))