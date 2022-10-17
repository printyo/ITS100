import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-3 * np.pi,3 * np.pi, 0.1)
print(x)

y1 = np.sin(x)
y2 = np.sin(x + 0.5)
y3 = np.sin(x + 1)
y4 = np.sin(x + 1.5)
print(y1)
print(y2)
print(y3)
print(y4)

#np.xlim(-3*np.pi,3*np.pi)
plt.plot(x, y4, color="pink", linewidth=2, linestyle="solid")
plt.plot(x, y3, color="orange", linewidth=2, linestyle="dashdot")
plt.plot(x, y2, color="green", linewidth=2, linestyle="dashed")
plt.plot(x, y1, color="blue", linewidth=2, linestyle="dotted")

#plt.show()
plt.savefig("Main.png")