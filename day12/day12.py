import re

def getInput(filename):
	
	graph = {}
	file = open(filename)
	for line in file:
		nodes = list(map(lambda x:int(x), re.findall(r"[0-9]+", line.rstrip("\n"))))
		graph[nodes[0]] = nodes[1:]

	return graph

def dfs(graph, node, visited):
	visited[node] = 1
	for neigh in graph[node]:
		if not neigh in visited:
			dfs(graph, neigh, visited)

def main():
	filename = "in.txt"
	graph = getInput(filename)
	visited = {}
	groups = 0
	for i in range(0, max(graph) + 1):
		if not i in visited:
			groups += 1
			dfs(graph, i, visited)
		if i == 0:
			print("Part 1: %d"%len(visited))
	print("Part 2: %d"%groups)

if __name__ == "__main__":
	main()