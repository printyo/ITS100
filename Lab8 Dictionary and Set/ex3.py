seq1 = input("Input sequence1: ").split()
seq2 = input("Input sequence2: ").split()

set1, set2 = set(), set()

for i in seq1:
  if i.isnumeric():
    set1.add(i)
for i in seq2:
  if i.isnumeric():
    set2.add(i)

if set1 == set2:
  print("Output: same set")
else:
  print("Output: different set")

