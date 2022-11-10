import numpy as np

data = np.loadtxt("Lab10 Numerical Computing/sales.tsv", delimiter='\t', dtype=float) #import file

branch = data[0:,0] #took first column of branch id
prodSale = data[0:,1:] #took total product sales

summ = np.sum(prodSale, axis =1) #get sum of each row
order = np.sort(summ) #sort into ascending order

n = len(order) - 1 #this code block reverses the array
lis = []
while n >=0:
    lis.append(order[n])
    n -= 1
myArr = np.array(lis) #turn back to matrix why not idk

myList = []
for i in range(5):
    myList.append([branch[i],summ[i]])
myArray = np.array(myList) #join branch id with sum product sold to corresponding branch

for j in range(5): #loop to find branch from max to min
    for i in range(5):
        if myArr[j] == myArray[i,1]:
            print(myArray[i])



