import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def func(b):
	p = random.randint(0, 4)
	dataY[p] += 1
	for i, b in dataY:
		b.setheight(dataY[i])

s = "hello world"

fig = plt.figure()
dataX = [1,2,3,4,5]
dataY = [0,0,0,0,0]
plt.xlim(0,5)
plt.ylim(0,5)
bar = plt.bar(dataX, dataY)

line_ani = animation.FuncAnimation(fig, func, 25, fargs=(),
                                   interval=50, blit=True)
plt.show()