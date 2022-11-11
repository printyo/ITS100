import numpy as np

data = np.loadtxt("sales.tsv", delimiter='\t', dtype=float) #import files

sales = data[:,1:]#takes only the sales excluding branch num
total = np.sum(sales,axis=1)#sum each row axis=1 is horizontal

sortAsc = np.sort(total)#sort into ascending order

num = len(data)-1 #this code block reverses the sorted order
myList = []
while num >= 0:
  myList.append(sortAsc[num])
  num -= 1
sortSumDesc = np.array(myList)#convert list -> matrix

myList = [] #this code block gets [branchnum, totalsum] of all elements
for i in range(len(data)):
  myList.append([data[i,0], total[i]])
myArr = np.array(myList)

print("Branch | Total Sales") #not needed just extra

for i in range(len(data)):# loops to find when branch num and total sum = sorted order
  for j in range(len(data)):
    if sortSumDesc[i] == myArr[j,1]:
      print(myArr[j])#prints the correct sorted row