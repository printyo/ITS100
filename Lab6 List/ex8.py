string = input("Enter a string: ")
new = ""
for i in string:
  if i.isalpha():
    if i.isupper():
      new += i.lower()
    else:
      new += i.upper()
  else:
    new += i
print("Reverse string output: %s"%new)