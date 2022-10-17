time = int(input("Input parking time (in minutes): "))
hour = time // 60
remain = time % 60
if remain <= 15:
  print("The charge is %d baht."%(hour*20))
else:
  print("The charge is %d baht."%(hour*20 + 20))