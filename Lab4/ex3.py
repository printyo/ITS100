day = int(input("Input number of days: "))
hour = int(input("Input number of hours: "))
print("Please select a choice:")
print("1-to calculate the total number of seconds or 2-to calculate the total number of minutes:")
choice = input("Enter your selected choice: ")
print("------------------------------------------------")
if choice == "1":
  second = 86400 * day + 3600 * hour
  print("The total number of minutes are %d."%second)
elif choice == "2":
  minute = 1440 * day + 60 * hour
  print("The total number of minutes are %d."%minute)