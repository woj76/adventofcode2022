#!/usr/bin/python3

import heapq
from collections import defaultdict

file = open("../data/day12.txt", "rt")
data = [list(x) for x in file.read().split('\n') if x != '']
file.close()

part2 = True

y_size = len(data)
x_size = len(data[0])

def n(x, y):
	r = [(x-1,y), (x+1,y), (x,y-1), (x, y+1)]
	r = [(xx,yy) for xx,yy in r if xx != -1 and xx != x_size and yy != -1 and yy != y_size]
	if part2:
		r = [(xx,yy) for xx,yy in r if ord(data[y][x]) - 1 <= ord(data[yy][xx])]
	else:
		r = [(xx,yy) for xx,yy in r if ord(data[y][x]) + 1 >= ord(data[yy][xx])]
	return r

ES = set()

for y in range(y_size):
	for x in range(x_size):
		if data[y][x] == 'S':
			data[y][x] = 'a'
			if not part2:
				S = (x,y)
		if data[y][x] == 'E':
			data[y][x] = 'z'
			if part2:
				S = (x,y)
			else:
				ES.add((x,y))
		if part2 and data[y][x] == 'a':
				ES.add((x,y))

visited = set()
q = []
dist = defaultdict(lambda : float('inf'))

dist[S] = 0
heapq.heappush(q, (0, S))

while q:
	_, u = heapq.heappop(q)
	visited.add(u)
	if u in ES:
		break
	for v in [y for y in n(u[0],u[1]) if y not in visited]:
		alt = dist[u] + 1
		if alt < dist[v]:
			dist[v] = alt
			heapq.heappush(q, (alt, v))

for e in ES:
	d = dist[e]
	if d < float('inf'):
		print(f"Part {2 if part2 else 1}: {d}")
