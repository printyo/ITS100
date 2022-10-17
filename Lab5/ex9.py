h = int(input("Height: "))
if h < 1:
  print("Error")
else:
  start = h - 1
  for i in range(1,h+1):
    print("#"*start+"."*(i*2-1)+"#"*start)
    start -= 1