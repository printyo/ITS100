import numpy as np

data = np.loadtxt("Lab10 Numerical Computing/sales.tsv", delimiter='\t', dtype=float)

branch = data[0:,0]
prodSale = data[0:,1:]

summ = np.sum(prodSale, axis =1)
print(summ)
indices = np.argsort(summ,kind="mergesort")

print(branch,summ, indices)
n = 0
m = 0
myList = []
for j in range(len(summ)):
    for i in indices:
        if i == n:
            myList.append([branch[m],summ[m]])
            n += 1
        m +=1
    m = 0
    
print(myList)
#yung mai sedß