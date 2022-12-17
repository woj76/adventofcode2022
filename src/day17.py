#!/snap/bin/pypy3

f = open("../data/day17.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [-1 if x=='<' else 1 for x in input_data]

x_min,x_max = 0,8

shape1 = [(0,0),(1,0),(2,0),(3,0)]
shape2 = [(1,2),(0,1),(1,1),(2,1),(1,0)]
shape3 = [(2,2),(2,1),(0,0),(1,0),(2,0)]
shape4 = [(0,0),(0,1),(0,2),(0,3)]
shape5 = [(0,1),(1,1),(0,0),(1,0)]

shapes = [shape1, shape2, shape3, shape4, shape5]

playfield = {}

blocks = 0
d = 0
s = 0

sd = {}

y_max = 0

for x in range(x_min+1,x_max):
	playfield[(x,y_max)] = True

while blocks < (1000000000000 if part2 else 2022):
	if part2:
		if (s,d) in sd:
			if 1000000000000 % (blocks - sd[(s,d)][0]) == sd[(s,d)][0]:
				h = y_max-sd[(s,d)][1]
				b = blocks-sd[(s,d)][0]
				r = sd[(s,d)][1]
				y_max = h*(1000000000000//b)+r
				break
		else:
			sd[(s,d)] = (blocks,y_max)
	blocks += 1

	i = 0
	y = y_max + 4
	x = 3
	shape = shapes[s]
	s = (s+1) % len(shapes)
	while True:
		if i % 2 == 0:
			nx = x + data[d]
			ny = y
			for sx,sy in shape:
				if not (x_min < sx+nx < x_max) or (sx+nx,sy+ny) in playfield:
					nx = x
					break
			d = (d + 1) % len(data)
		else:
			ny -= 1
			nx = x
			free = True
			for sx,sy in shape:
				if (sx+nx,sy+ny) in playfield:
					free = False
					break
			if not free:
				for sx,sy in shape:
					playfield[(x+sx,y+sy)] = True
					y_max = max(y_max,y+sy)
				break
		x = nx
		y = ny
		i += 1

print(f"Part {2 if part2 else 1}: {y_max}")
