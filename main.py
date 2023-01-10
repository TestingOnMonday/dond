# import modules here
import os # for clearing screen
import random as r # for randomizing the order of cases

# variables and constants here
MONEY = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10_000, 25_000, 75_000, 100_000, 200_000, 300_000, 400_000, 500_000, 750_000, 1_000_000] # all the money values in Deal or No Deal
CASES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26] # list of the case numbers in Deal or No Deal
vals = [] # list to keep track of everything lmao

# functions here
def setup(): # sets up the vals list to use for the game
	global order
	order = []
	order = order + CASES
	r.shuffle(order) # shuffles the case order to use when drawing the screen
	for i in range(26): # shuffles the money value in each case, and then appends the cases list, true, and the randomly assigned money value
		print(i)
		#ndom_money = r.shuffle(MONEY)
		#vals.append(CASES[i])
		#vals.append(True)
		#vals.append(random_money[i])
		

# main loop
setup()
print(vals)
while True:
	break
# remember list.index() lmao

