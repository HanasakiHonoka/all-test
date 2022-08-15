# import requests
#
# res = requests.get("http://www.getchu.com/all/month_title.html?genre=pc_soft&gage=&year=2021&month=06")
#
# print(res.text)

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
plt.show()