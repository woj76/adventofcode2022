#!/usr/bin/python3

import sys,math

sys.setrecursionlimit(2000)

f = open("../data/day24.txt", "rt")
input_data = f.read()
f.close()

part2 = True

p = [x for x in input_data.split('\n') if x != '']

bs = {'<':[],'>':[],'v':[],'^':[]}

for y,l in enumerate(p):
	for x,c in enumerate(l):
		if c == '<' or c == '>' or c == 'v' or c == '^':
			bs[c].append((x-1,y-1))

x_max = len(p[0])-2
y_max = len(p)-2

start = (0,-1)
end = (x_max-1,y_max)

lcm = x_max * y_max // math.gcd(x_max,y_max)

for c in ['<','>','v','^']:
	l = bs[c]
	d = {}
	for x in l:
		d[x] = True
	bs[c] = d

moves = {}

for i in range(lcm):
	free = {}
	for x in range(x_max):
		for y in range(y_max):
			if (x,y) not in bs['<'] and (x,y) not in bs['>'] and (x,y) not in bs['v'] and (x,y) not in bs['^']:
				free[(x,y)] = '.'
	free[start] = '.'
	free[end] = '.'
	moves[i] = free
	bs['<'] = [((x-1)%x_max,y) for x,y in bs['<']]
	bs['>'] = [((x+1)%x_max,y) for x,y in bs['>']]
	bs['v'] = [(x,(y+1)%y_max) for x,y in bs['v']]
	bs['^'] = [(x,(y-1)%y_max) for x,y in bs['^']]
	for c in ['<','>','v','^']:
		l = bs[c]
		d = {}
		for x in l:
			d[x] = True
		bs[c] = d

visited = {}

min_path = 1000

def search_path(x,y,step,path_len,state):
	global min_path
	if state == 0 and (x,y) == end:
		state = 1
	elif state == 1 and (x,y) == start:
		state = 2
	elif state == 2 and (x,y) == end:
		state = 3
	if (x,y) == end and state == 3:
		if path_len < min_path:
			min_path = path_len
		return path_len
	if path_len >= min_path:
		return float('inf')
	if (x,y,step,state) in visited and visited[(x,y,step,state)] <= path_len:
		return float('inf')
	visited[(x,y,step,state)] = path_len
	path_len += 1
	step = (step+1) % lcm
	m = moves[step]
	r = float('inf')
	for nx,ny in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
		if (x+nx,y+ny) in m:
			r = min(r,search_path(x+nx,y+ny,step,path_len,state))
	return r

res = search_path(start[0],start[1],0,0,0 if part2 else 2)

print(f"Part {2 if part2 else 1}: {res}")
