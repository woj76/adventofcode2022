#!/usr/bin/python3

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
max_pressure = float('-inf')

total_time = 25 if part2 else 29

all_valves = len(active_valves)

def search_max1(curr_time, total_pressure, curr_valve, open_valves, producing_valves, second):
	global max_pressure

	if curr_time == total_time:
		if second:
			max_pressure = max(max_pressure, total_pressure)
			return
		else:
			search_max1(0, total_pressure, mapping['AA'], open_valves, {}, True)
			return

	ovs = "".join(sorted(open_valves.keys()))
	pvs = "".join(sorted(producing_valves.keys()))
	s = chr(33+curr_time) + curr_valve + ovs + pvs
	if s in visited and visited[s] >= total_pressure:
		return
	visited[s] = total_pressure

	if len(open_valves.keys()) == all_valves:
		nt = total_pressure
		for ov in producing_valves:
			nt += (total_time-curr_time)*active_valves[ov]
		search_max1(total_time, nt, curr_valve, open_valves, producing_valves, second)
		return

	ext_time = 0
	if curr_valve not in open_valves and curr_valve in active_valves:
		producing_valves_copy = producing_valves.copy()
		open_valves_copy = open_valves.copy()
		open_valves_copy[curr_valve] = curr_time
		producing_valves_copy[curr_valve] = True
		ext_time = 1
	else:
		open_valves_copy = open_valves
		producing_valves_copy = producing_valves
	for v,d in distances[curr_valve]:
		if d == 0:
			continue
		if curr_time + d + ext_time >= total_time:
			d = total_time - curr_time - ext_time
		nt = total_pressure
		for ov in producing_valves_copy:
			nt += (d+ext_time)*active_valves[ov]
		search_max1(curr_time+d+ext_time, nt, v, open_valves_copy, producing_valves_copy, second)

if part2:
	search_max1(0,0,mapping['AA'],{},{},False)
else:
	search_max1(0,0,mapping['AA'],{},{},True)

print(f"Part {2 if part2 else 1}: {max_pressure}")
