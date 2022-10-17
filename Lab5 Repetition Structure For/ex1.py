even = 0
odd = 0
for i in range(5):
  x = int(input("enter a number "))
  if x % 2 == 0:
    even += 1
  else:
    odd += 1
print("there were %d even numbers"%even)
print("there were %d odd numbers"%odd)