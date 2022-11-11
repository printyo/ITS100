import numpy as np

data = np.loadtxt("sales.tsv", delimiter='\t', dtype=float)

sales = data[:,1:]
total = np.sum(sales,axis=1)

sortAsc = np.sort(total)

num = len(data)-1
myList = []
while num >= 0:
  myList.append(sortAsc[num])
  num -= 1
sortSumDesc = np.array(myList)
myList = []
for i in range(len(data)):
  myList.append([data[i,0], total[i]])
myArr = np.array(myList)

print("Branch | Total Sales")

for i in range(len(data)):
  for j in range(len(data)):
    if sortSumDesc[i] == myArr[j,1]:
      print(myArr[j])