import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

## Runtime Variables ###
numberPlayers = 1000
tradingRounds = 30
startingCash  = 50
proportion = 2
frame_rate = 10 #milliseconds
########################

def animate(i):
	p = random.randint(0, 10)
	l = random.randint(0,10)
	dataY[p] += 1
	dataY[l] -= 1
	ax1.clear()
	ax1.bar(dataX, dataY)

def animateTrading(i):
	global broke, round_num
	random.shuffle(player_worth)
	for i in range(0,len(player_worth) / proportion, 2):
		p = random.randint(0,100)
		if p > 50:
			if player_worth[i+1] != 0:
				player_worth[i] += 1
				player_worth[i+1] -= 1
		else:
			if player_worth[i] != 0:
				player_worth[i+1] += 1
				player_worth[i] -= 1
		# broke player exclusion
		'''
		if player_worth[i] == 0:
			broke += 1
			del player_worth[i]
		if player_worth[i+1] == 0:
			broke += 1
			del player_worth[i+1]
		'''

		#build graph data
	dataX, dataY = buildReport(player_worth)
	ax1.clear()
	ax1.bar(dataX,dataY)
	ax1.set_xlabel('wealth in $')
	ax1.set_ylabel("number of players")
	ax1.set_title("Random Trading: Round " + str(round_num))
	round_num += 1




def buildReport(playerData):
	dataX = range(0,max(playerData)+1)
	dataY = [0] * (max(playerData)+1)
	for pWorth in playerData:
		dataY[pWorth] += 1
	return dataX, dataY

player_worth = [startingCash] * numberPlayers
#global broke
broke = 0
round_num = 1

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


dataX = range(0,max(player_worth)+1)
dataY = [0] * (max(player_worth) + 1)
playerData = [10] * numberPlayers

ani = animation.FuncAnimation(fig, animateTrading, 25, interval=frame_rate)
plt.show()