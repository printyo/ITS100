import random as r
lis = []
for i in range(1,5):
  x = input("Enter string#%d: "%i)
  lis.append(x)
r.shuffle(lis)
print("Random order of sentence:",lis[0],lis[1],lis[2],lis[3])