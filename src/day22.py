#!/usr/bin/python3

f = open("../data/day22.txt", "rt")
input_data = f.read()
f.close()

data = input_data.split('\n\n')

part2 = True

p = data[0].split('\n')
moves = data[1].strip().replace('L',' L ').replace('R',' R ').split(' ')

plane = {}

x = y = None

for yy,l in enumerate(p):
	for xx,c in enumerate(l):
		if c == '#' or c == '.':
			if x == None and y == None:
				x,y = xx,yy
			plane[(xx,yy)] = c

directions = [(1,0),(0,1),(-1,0),(0,-1)]
dir = 0

def id_wall(x,y):
	x = x // 50
	y = y // 50
	if x == 1 and y == 0:
		return 0
	if x == 2 and y == 0:
		return 1
	if x == 1 and y == 1:
		return 2
	if x == 0 and y == 2:
		return 3
	if x == 1 and y == 2:
		return 4
	if x == 0 and y == 3:
		return 5

change_dirs = {}
change_dirs[(0,2)] = 0
change_dirs[(0,3)] = 0
change_dirs[(1,1)] = 2
change_dirs[(1,0)] = 2
change_dirs[(1,3)] = 3
change_dirs[(2,0)] = 3
change_dirs[(2,2)] = 1
change_dirs[(3,2)] = 0
change_dirs[(3,3)] = 0
change_dirs[(4,1)] = 2
change_dirs[(4,0)] = 2
change_dirs[(5,1)] = 1
change_dirs[(5,0)] = 3
change_dirs[(5,2)] = 1

def transfer(x,y,wall_id,dir):
	if wall_id == 0 and dir == 2:
		assert x == 50 and 0<=y<50
		return 0,100+(49-y)
	if wall_id == 3 and dir == 2:
		assert x == 0 and 100<y<=150
		return 50,(49-(y%50))
	if wall_id == 0 and dir == 3:
		assert y == 0 and 50<=x<100
		return 0,150+(x%50)
	if wall_id == 5 and dir == 2:
		assert x == 0 and 150<=y<200
		return 50+(y%50),0
	if wall_id == 1 and dir == 0:
		assert x == 149 and 0<=y<50
		return 99,100+(49-y)
	if wall_id == 4 and dir == 0:
		assert x == 99 and 100<=y<150
		return 149,49-(y%50)
	if wall_id == 1 and dir == 3:
		assert y == 0 and 100<=x<150
		return (x%50),199
	if wall_id == 5 and dir == 1:
		assert y == 199 and 0<=x<50
		return 100+(x%50),0
	if wall_id == 1 and dir == 1:
		assert y == 49 and 100<=x<150
		return 99,50+(x%50)
	if wall_id == 2 and dir == 0:
		assert x == 99 and 50<=y<100
		return 100+(y%50),49
	if wall_id == 2 and dir == 2:
		assert x == 50 and 50<=y<100
		return (y%50),100
	if wall_id == 3 and dir == 3:
		assert y == 100 and 0<=x<50
		return 50,50+x
	if wall_id == 4 and dir == 1:
		assert y == 149 and 50<=x<100
		return 49,150+(x%50)
	if wall_id == 5 and dir == 0:
		assert x == 49 and 150<=y<200
		return 50+(y%50),149

for m in moves:
	if m == 'L':
		dir = (dir-1) % len(directions)
		continue
	if m == 'R':
		dir = (dir+1) % len(directions)
		continue
	for _ in range(int(m)):
		dx,dy = directions[dir]
		nx,ny = x+dx,y+dy
		if part2:
			if (nx,ny) not in plane:
				wall_id = id_wall(x,y)
				nx,ny = transfer(x,y,wall_id,dir)
				if plane[(nx,ny)] == '.':
					dir = change_dirs[(wall_id,dir)]
		else:
			if (nx,ny) not in plane:
				nx,ny = x,y
				while (nx-dx,ny-dy) in plane:
					nx,ny = nx-dx,ny-dy
		if plane[(nx,ny)] == '#':
			break
		x,y=nx,ny

print(f"Part {2 if part2 else 1}: {1000*(y+1)+4*(x+1)+dir}")
