import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

## Runtime Variables ###
numberPlayers = 1000
tradingRounds = 30
startingCash  = 10
testing = False
########################

def animate(i):
	p = random.randint(0, 10)
	dataY[p] += 1
	ax1.clear()
	ax1.bar(dataX, dataY)

player_worth = [10] * numberPlayers

fig = plt.figure()
#dataX = [1,2,3,4,5,6,7,8,9,10]
dataX = range(0,max(player_worth)+1)
print dataX
dataY = [0] * (max(player_worth) + 1)
ax1 = fig.add_subplot(1,1,1)



ani = animation.FuncAnimation(fig, animate, 25, interval=1000)
plt.show()