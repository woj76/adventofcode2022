#!/usr/bin/python3

f = open("../data/day23.txt", "rt")
input_data = f.read()
f.close()

part2 = True

p = input_data.split('\n')

plane = {}

for y,l in enumerate(p):
	for x,c in enumerate(l):
		if c == '#':
			plane[(x,y)] = c

rounds = 0
d = 0

directions = [[(-1,-1),(0,-1),(1,-1)],[(-1,1),(0,1),(1,1)],[(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)]]

while part2 or rounds < 10:
	move_to = {}
	propose = {}
	for x,y in plane:
		ns = False
		for nx,ny in [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]:
			if (x+nx,y+ny) in plane:
				ns = True
				break
		if ns:
			for i in range(4):
				dir = directions[(d+i)%len(directions)]
				to_check = []
				for j in range(3):
					to_check.append((x+dir[j][0],y+dir[j][1]))
				if to_check[0] not in plane and to_check[1] not in plane and to_check[2] not in plane:
					np = to_check[1]
					propose[(x,y)] = np
					if np not in move_to:
						move_to[np] = 1
					else:
						move_to[np] += 1
					break
	new_plane = {}
	moved = False
	for x,y in plane:
		if (x,y) in propose and move_to[propose[(x,y)]] == 1:
			new_plane[propose[(x,y)]] = '#'
			moved=True
		else:
			new_plane[(x,y)] = '#'
	plane = new_plane
	d = (d+1) % len(directions)
	rounds += 1
	if part2 and not moved:
		break

if part2:
	res = rounds
else:
	x_min = float('inf')
	x_max = float('-inf')
	y_min = float('inf')
	y_max = float('-inf')

	for x,y in plane:
		x_min = min(x,x_min)
		x_max = max(x,x_max)
		y_min = min(y,y_min)
		y_max = max(y,y_max)

	res = (x_max-x_min+1)*(y_max-y_min+1) - len(plane)

print(f"Part {2 if part2 else 1}: {res}")
