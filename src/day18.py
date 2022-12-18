#!/snap/bin/pypy3

from collections import deque

f = open("../data/day18.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [tuple([int(y) for y in x.split(',')]) for x in input_data.split('\n') if x != ""]

plane = {}

sides = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

if part2:
	x_min,x_max = float('inf'),float('-inf')
	y_min,y_max = float('inf'),float('-inf')
	z_min,z_max = float('inf'),float('-inf')

for d in data:
	plane[d] = True
	if part2:
		x_min,x_max = min(x_min,d[0]),max(x_max,d[0])
		y_min,y_max = min(y_min,d[1]),max(y_max,d[1])
		z_min,z_max = min(z_min,d[2]),max(z_max,d[2])

if part2:
	x_min -= 2
	x_max += 2
	y_min -= 2
	y_max += 2
	z_min -= 2
	z_max += 2
	ext = {}
	for x in range(x_min,x_max+1):
		for y in range(y_min,y_max+1):
			ext[(x,y,z_min)] = True
			ext[(x,y,z_max)] = True
	for x in range(x_min,x_max+1):
		for z in range(z_min,z_max+1):
			ext[(x,y_min,z)] = True
			ext[(x,y_max,z)] = True
	for y in range(y_min,y_max+1):
		for z in range(z_min,z_max+1):
			ext[(x_min,y,z)] = True
			ext[(x_max,y,z)] = True
	q = deque([(x_min+1,y_min+1,z_min+1)])
	while q:
		(x,y,z) = q.popleft()
		ext[(x,y,z)] = True
		for sx,sy,sz in sides:
			n = (x+sx,y+sy,z+sz)
			if n not in plane and n not in ext and n not in q:
				q.append(n)

res = 0

for px,py,pz in plane:
	for sx,sy,sz in sides:
		p = (px+sx,py+sy,pz+sz)
		if part2:
			if p in ext:
				res += 1
		else:
			if p not in plane:
				res += 1

print(f"Part {2 if part2 else 1}: {res}")
