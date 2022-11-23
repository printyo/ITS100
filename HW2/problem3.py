score = 0
word = input("Input a word: ")
if word.isalpha() == False:
  print("Invalid input")
else:
  for i in word:
    i = i.lower()
    if i in "aeilnorstu":
      score += 1
    elif i in "dg":
      score += 2
    elif i in "bcmp":
      score += 3
    elif i in "fhvwy":
      score += 4
    elif i in "k":
      score += 5
    elif i in "jx":
      score += 8
    elif i in "qz":
      score += 10
  print("Output:",score)