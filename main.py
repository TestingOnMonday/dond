# import modules here
import os # for clearing screen
import random as r # for randomizing the order of cases
# variables and constants here
MONEY = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10_000, 25_000, 75_000, 100_000, 200_000, 300_000, 400_000, 500_000, 750_000, 1_000_000] # all the money values in Deal or No Deal
CASES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25] # list of the case numbers in Deal or No Deal
vals = [] # list to keep track of everything lmao

# functions here
def setup(): # sets up the vals list to use for the game
	global order
	order = []
	order = order + CASES # sets up the order for later
	random_money = []
	random_money = random_money + MONEY # assigns money values
	r.shuffle(order) # shuffles the case order to use when drawing the screen
	for i in range(25): # shuffles the money value in each case, and then appends the cases list, true, and the randomly assigned money value
		vals.append(CASES[i])
		vals.append(True)
		vals.append(random_money[i])

def render(): # prints the random case values like in the game
	j = 0 #initializes the bump up value or whatever
	for i in range(5): 
		for k in range(5):
			if len(str(order[i+k + 4*j])) == 1: #checks if the value is a 0
					print("", order[i+k + 4*j], end="  ") # prints an extra space
			else:
					print(order[i+k + 4*j], end="  ") # prints normally
		print('') # adds a new line
		j+=1 # changes the bump up value

# main program
print('Deal or No Deal')
setup()
while True:
	render()
	break
# remember list.index() lmao 