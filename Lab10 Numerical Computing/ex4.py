import numpy as np

data = np.loadtxt("Lab10 Numerical Computing/sales.tsv", delimiter='\t', dtype=float)

branch = data[0:,0]
prodSale = data[0:,1:]
print(branch)

summ = np.sum(prodSale, axis =1)
    
print(summ)
lis = []
for i in range(len(branch)):
    lis.append([branch[i],summ[i]])
    
lis.sort(reverse=True)
print(lis) 

#yung mai sedß