import re

def getInput(filename):
	gates = {}
	for line in open(filename):
		g = list(map(lambda x: int(x), re.findall(r"[0-9]+", line.rstrip("\n"))))
		gates[g[0]] = g[1]
	return gates

def runThroughGates(gates, startTime=0):
	time = startTime
	pos = 0
	end = max(gates)
	timesCaught = 0
	severityOfTrip = 0

	while pos < end + 1:
		# check if on a tile with scanner
		if pos in gates:
			# check if scanner on top:
			if time % ((gates[pos] - 1) * 2) == 0:
				timesCaught += 1
				severityOfTrip += pos * gates[pos]
				if startTime != 0:
					break
		pos += 1
		time += 1

	return timesCaught, severityOfTrip

def getWaitTime(gates):
	start = 1
	while True:
		timesCaught, _ = runThroughGates(gates, start)
		if timesCaught == 0:
			break
		start += 1

	return start

def main():
	gates = getInput("in.txt")
	_, severityOfTrip = runThroughGates(gates)
	print("Part 1: %d"%severityOfTrip)
	waitTime = getWaitTime(gates)
	print("Part 2: %d"%waitTime)

if __name__ == "__main__":
	main()