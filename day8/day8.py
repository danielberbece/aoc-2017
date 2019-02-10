# Python 3
from parse import *

def getInput(filename):
	file = open(filename)
	lines = []
	for line in file:
		p = parse("{} {} {} if {} {} {}", line.rstrip("\n"))
		lines.append(p.fixed)

	return lines

def runProgram(instructions, regs):
	highestValueEver = 0
	for i in instructions:
		#check if:
		ifreg = 0
		if i[3] in regs:
			ifreg = regs[i[3]]
		ok = 0

		if i[4] == '>' and ifreg > int(i[5]):
			ok = 1
		elif i[4] == '<' and ifreg < int(i[5]):
			ok = 1
		elif i[4] == '<=' and ifreg <= int(i[5]):
			ok = 1
		elif i[4] == '>=' and ifreg >= int(i[5]):
			ok = 1
		elif i[4] == '==' and ifreg == int(i[5]):	
			ok = 1
		elif i[4] == '!=' and ifreg != int(i[5]):	
			ok = 1
		
		if ok == 1:
			if i[1] == 'inc':
				if i[0] in regs:
					regs[i[0]] += int(i[2])
				else:
					regs[i[0]] = int(i[2])
			elif i[1] == 'dec':
				if i[0] in regs:
					regs[i[0]] -= int(i[2])
				else:
					regs[i[0]] = -int(i[2])
			if highestValueEver < regs[i[0]]:
				highestValueEver = regs[i[0]]
	print("Part 1: %d"%getMaxValue(regs))
	print("Part 2: %d"%highestValueEver)

def getMaxValue(regs):
	return max(regs.values())

def main():
	instructions = getInput("in.txt")
	regs = {}
	runProgram(instructions, regs)

if __name__ == "__main__":
	main()