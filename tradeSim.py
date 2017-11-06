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
	l = random.randint(0,10)
	dataY[p] += 1
	dataY[l] -= 1
	ax1.clear()
	ax1.bar(dataX, dataY)

def buildReport(playerData):
	dataX = range(0,max(playerData)+1)
	dataY = [0] * (max(playerData)+1)
	for pWorth in playerData:
		dataY[pWorth] += 1
	return dataX, dataY

player_worth = [10] * numberPlayers

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

dataX = range(0,max(player_worth)+1)
dataY = [0] * (max(player_worth) + 1)
playerData = [10] * numberPlayers

ani = animation.FuncAnimation(fig, animate, 25, interval=500)
plt.show()