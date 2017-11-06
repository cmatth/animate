import matplotlib.pyplot as plt
import matplotlib.animation as anime
import random


## Runtime Variables ###
numberPlayers = 1000
tradingRounds = 30
startingCash  = 10
testing = False
########################

def tradingRound(bar):

	traded_players = []
	random.shuffle(players)
	while(len(players) >= numberPlayers / 2):
		p = random.uniform(0,1000)
		#testing
		if testing:
			print "players left: ", len(players)
			print "p1: ", players[0], "p2: ", players[1]
			print "$s in pool: ", sum(players) + sum(traded_players)
		#######
		if p >= 500:
			players[0] += 1
			players[1] -= 1
		else:
			players[0] -= 1
			players[1] += 1
		#testing
		if testing:
			print "p1: ", players[0], "p2: ", players[1]
			print "####################"
		########
		if players[0] == 0:
			broke_players += 1
			traded_players.append(players[1])
			del players[0]
			del players[0]
		elif players[1] == 0:
			broke_players += 1
			traded_players.append(players[0])
			del players[0]
			del players[0]
		else:
			traded_players.append(players[0])
			traded_players.append(players[1])
			del players[0]
			del players[0]
		#testing
		if testing:
			raw_input()
		########

	x_data = range(0, max(players) + 1)
	y_data = [0] * (len(x_data))
	y_data[0] = broke_players
	for i in range(1, len(x_data)):
		y_data[players[i]] += 1
	bar = plt.bar(x_data, y_data)
	return bar

players = []
for x in range(0,numberPlayers):
	players.append(startingCash)

broke_players = 0
x_data = range(0, max(players) + 1)
y_data = [0] * (len(x_data))
y_data[0] = broke_players
for i in range(1, len(x_data)):
	y_data[players[i]] += 1

fig1 = plt.figure()
bar = plt.bar(x_data,y_data)
plt.xlabel('wealth in $')
plt.ylabel('# of players')
plt.title('Random Trading Game')
ani = anime.FuncAnimation(fig1, tradingRound, 1000, fargs=(), interval=50)
plt.show()

if testing:
	print "Players left in pool: ", len(players)
	print "  Players gone broke: ", broke_players
	print "      Richest player: ", "$" + str(max(players))
	print "     Total $ in pool:", sum(players)

