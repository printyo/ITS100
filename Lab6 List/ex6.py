cal = input("Enter dd/mm/yyyy: ")
if len(cal) == 8:
  date = cal[:2]
  mon = cal[2:4].strip("0")
  yr = int(cal[4:]) - 543
  if int(mon) > 12:
    print("Error! There're 12 months")
  else:
    print("Date = %s"%date)
    print("Month = %s"%mon)
    print("Year = %d"%yr)
else:
  print("Please enter 8 digits!!")
