#!/usr/bin/python3

f = open("../data/day09.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [x for x in input_data.split('\n') if x != '']

hx = hy = 0

tails = []
for i in range(9 if part2 else 1):
	tails.append((0,0))

tvisited = {tails[-1]:True}

dirs = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
deltas = {-2:-1,-1:-1,0:0,1:1,2:1}

for d in data:
	[dir,steps] = d.split(' ')
	dx,dy = dirs[dir]
	steps = int(steps)
	for _ in range(steps):
		hx += dx
		hy += dy
		px = hx
		py = hy
		for i in range(len(tails)):
			tx,ty = tails[i]
			sx = px - tx
			sy = py - ty
			if abs(sx) > 1 or abs(sy) > 1:
				tx += deltas[sx]
				ty += deltas[sy]
			tails[i] = (tx,ty)
			px = tx
			py = ty
		tvisited[(tx,ty)] = True

print(len(tvisited))
