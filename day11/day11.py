# Python 3
import re

def getInput(filename):
	file = open(filename)
	lines = []
	for line in file:
		lines = re.findall(r"[^,]+", line.rstrip("\n"))

	return lines

def moveOptim(dirs, move):
	if move == 'n':
		if dirs[1] != 0:
			dirs[1] -= 1
		elif dirs[4] != 0:
			dirs[4] -= 1
			moveOptim(dirs, 'ne')
		elif dirs[5] != 0:
			dirs[5] -= 1
			moveOptim(dirs, 'nw')
		else:
			dirs[0] += 1
	elif move == 's':
		if dirs[0] != 0:
			dirs[0] -= 1
		elif dirs[2] != 0:
			dirs[2] -= 1
			moveOptim(dirs, 'se')
		elif dirs[3] != 0:
			dirs[3] -= 1
			moveOptim(dirs, 'sw')
		else:
			dirs[1] += 1
	elif move == 'ne':
		if dirs[5] != 0:
			dirs[5] -= 1
		elif dirs[1] != 0:
			dirs[1] -= 1
			moveOptim(dirs, 'se')
		elif dirs[3] != 0:
			dirs[3] -= 1
			moveOptim(dirs, 'n')
		else:
			dirs[2] += 1
	elif move == 'nw':
		if dirs[4] != 0:
			dirs[4] -= 1
		elif dirs[1] != 0:
			dirs[1] -= 1
			moveOptim(dirs, 'sw')
		elif dirs[2] != 0:
			dirs[2] -= 1
			moveOptim(dirs, 'n')
		else:
			dirs[3] += 1
	elif move == 'se':
		if dirs[3] != 0:
			dirs[3] -= 1
		elif dirs[0] != 0:
			dirs[0] -= 1
			moveOptim(dirs, 'ne')
		elif dirs[5] != 0:
			dirs[5] -= 1
			moveOptim(dirs, 's')
		else:
			dirs[4] += 1
	elif move == 'sw':
		if dirs[2] != 0:
			dirs[2] -= 1
		elif dirs[0] != 0:
			dirs[0] -= 1
			moveOptim(dirs, 'nw')
		elif dirs[4] != 0:
			dirs[4] -= 1
			moveOptim(dirs, 's')
		else:
			dirs[5] += 1

def findDistFromOrigin(steps):
	# Order: n, s, ne, nw, se, sw
	dirs = [0] * 6
	for s in steps:
		moveOptim(dirs, s)
		
	return sum(dirs)

def findLongestDist(steps):
	maxDist = 0
	dirs = [0] * 6
	for s in steps:
		moveOptim(dirs, s)
		if sum(dirs) > maxDist:
			maxDist = sum(dirs)
			
	return maxDist

def main():
	steps = getInput("in.txt")
	print("Part 1: %d"%findDistFromOrigin(steps))
	print("Part 2: %d"%findLongestDist(steps))

if __name__ == "__main__":
	main()