n = 0
s = 0
try:
  v = float(input("Input v: "))
except ValueError:
  print("Invalid input")
else:
  while s <= v:
    n += 1
    s = s + ((2**0.5)*(n)-1)
    
  print("Output: n = %d, S = %.2f"%(n,s))