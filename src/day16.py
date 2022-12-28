#!/snap/bin/pypy3

from collections import defaultdict

from heapq import heappush, heappop

def dijkstra(G, startingNode):
	visited = set()
	parentsMap = {}
	pq = []
	nodeCosts = defaultdict(lambda: float('inf'))
	nodeCosts[startingNode] = 0
	heappush(pq, (0, startingNode))

	while pq:
		_, node = heappop(pq)
		visited.add(node)
		for adjNode in G[node][1]:
			if adjNode in visited:
				continue
			newCost = nodeCosts[node] + 1
			if nodeCosts[adjNode] > newCost:
				parentsMap[adjNode] = node
				nodeCosts[adjNode] = newCost
				heappush(pq, (newCost, adjNode))
	return parentsMap, nodeCosts

f = open("../data/day16.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [x for x in input_data.split('\n') if x != '']

valves = {}
active_valves = {}

for d in data:
	[v,t] = d.split('; ')
	v = v.split(' ')
	r = int(v[4][5:])
	v = v[1]
	t = t[23 if "valves" in t else 22:].split(', ')
	valves[v] = (r,t)
	if r > 0:
		active_valves[v] = r

distances = {}

for n in ['AA'] + list(active_valves.keys()):
	distances[n] = []
	_, nc = dijkstra(valves,n)
	for an in nc.items():
		if an[0] in active_valves:
			distances[n].append(an)

mapping = {}

for i,k in enumerate(distances.keys()):
	mapping[k] = chr(33+i)

dist = {}
act_val = {}

for v,l in distances.items():
	dist[mapping[v]] = [(mapping[v],d) for (v,d) in l]

for v,f in active_valves.items():
	act_val[mapping[v]] = f

distances = dist
active_valves = act_val

visited = {}

total_time = 25 if part2 else 29

all_valves = len(active_valves)

bestests = {}

def search_max1(curr_time, total_pressure, curr_valve, open_valves):
	if curr_time == total_time:
		if part2 and (open_valves not in bestests or bestests[open_valves] <= total_pressure):
			bestests[open_valves] = total_pressure
		return total_pressure

	s = chr(33+curr_time) + curr_valve + open_valves
	if s in visited and visited[s] >= total_pressure:
		return float('-inf')
	visited[s] = total_pressure

	if len(open_valves) == all_valves:
		nt = total_pressure
		for ov in open_valves:
			nt += (total_time-curr_time)*active_valves[ov]
		return search_max1(total_time, nt, curr_valve, open_valves)

	ext_time = 0
	if curr_valve not in open_valves and curr_valve in active_valves:
		open_valves = "".join(sorted(list(open_valves + curr_valve)))
		ext_time = 1
	best = float('-inf')
	for v,d in distances[curr_valve]:
		if d == 0:
			continue
		if curr_time + d + ext_time >= total_time:
			d = total_time - curr_time - ext_time
		nt = total_pressure
		for ov in open_valves:
			nt += (d+ext_time)*active_valves[ov]
		best = max(best, search_max1(curr_time+d+ext_time, nt, v, open_valves))
	return best

res = search_max1(0, 0, mapping['AA'], "")

if part2:
	max_pressure = float('-inf')
	l = list(bestests.keys())
	for i in range(len(l)):
		for j in range(i+1,len(l)):
			x,y = l[i],l[j]
			if not [True for xy in x+y if xy in x and xy in y]:
				p = bestests[x]+bestests[y]
				if p > max_pressure:
					max_pressure = p
	res = max_pressure

print(f"Part {2 if part2 else 1}: {res}")
