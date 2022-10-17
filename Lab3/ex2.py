import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1,10.1,0.1)
print(x)
y = (1 + x)/(np.sqrt(x))
print(y)

#np.xlim(0,10)
plt.plot(x,y)
#plt.show()
plt.savefig("Main.png")