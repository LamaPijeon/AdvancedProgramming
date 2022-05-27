#  Simple Linear Regression
import numpy as np
import matplotlib.pyplot as plt

phones = np.array([[2001, 2003, 2005, 2010, 2016], [1000, 1025, 1500, 2000, 2500]])

plt.plot(phones[0], phones[1])
plt.ylabel('phone prices oer the years')
plt.axes([2000, 2030, 500, 3500])
plt.show()