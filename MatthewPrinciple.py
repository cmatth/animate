# Casey Matthews
# 11/06/17
# A random trading game simulation that demonstrates the economic
# phenomenon known as the Matthew Principle. A pool of players
# are given a fixed amount of capital and are then randomly
# paired for trading. In each transaction, the player has an
# equal chance to either gain or lose a dollar. You will see
# that in the early stages, the wealth becomes distributed
# normally but as the game progresses it collapses into a
# Pareto distribution. To those who have everything,more
# will be given and from those who have nothing everything
# will be taken -- this is the Matthew Principle.

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

## Runtime Variables ###
numberPlayers = 1000 	# number of players
startingCash  = 10 		# $ players start with
proportion = 3  		# 1 / n player trade each round.
frame_rate = 50 		#milliseconds
########################

def animateTrading(i):
	global broke, round_num
	random.shuffle(player_worth)
	for i in range(0, frequency, 2):
		p = random.randint(0,10000)
		if p > 5000:
			if player_worth[i+1] != 0:
				player_worth[i] += 1
				player_worth[i+1] -= 1
		else:
			if player_worth[i] != 0:
				player_worth[i+1] += 1
				player_worth[i] -= 1

	#build graph data
	dataX, dataY = buildReport(player_worth)
	ax1.clear()
	ax1.bar(dataX,dataY)
	ax1.set_xlabel('Wealth in $')
	ax1.set_ylabel("Number of Players")
	ax1.set_title("Random Trading: Round " + str(round_num))
	round_num += 1

def buildReport(playerData):
	dataX = range(0,max(playerData)+1)
	dataY = [0] * (max(playerData)+1)
	for pWorth in playerData:
		dataY[pWorth] += 1
	return dataX, dataY

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
player_worth = [startingCash] * numberPlayers
dataX = range(0,max(player_worth)+1)
dataY = [0] * (max(player_worth) + 1)

frequency = int(len(player_worth) / proportion)
round_num = 1

ani = animation.FuncAnimation(fig, animateTrading, 25, interval=frame_rate)
plt.show()