#!/snap/bin/pypy3

f = open("../data/day14.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [x for x in input_data.split('\n') if x != '']

plane = {}
max_y = float('-inf')

for d in data:
	d = d.split(' -> ')
	for i in range(1,len(d)):
		[x1,y1] = [int(z) for z in d[i-1].split(',')]
		[x2,y2] = [int(z) for z in d[i].split(',')]
		if x1 > x2:
			x1,x2 = x2,x1
		if y1 > y2:
			y1,y2 = y2,y1
		max_y = max(max_y,y2)
		if x1 == x2:
			for y in range(y1,y2+1):
				plane[(x1,y)] = '#'
		elif y1 == y2:
			for x in range(x1,x2+1):
				plane[(x,y1)] = '#'

stop_flow = False

while not stop_flow:
	xs,ys = (500,0)
	while True:
		ns = [(xs+0,ys+1),(xs-1,ys+1),(xs+1,ys+1)]
		for nx,ny in ns:
			if (nx,ny) not in plane:
				xs,ys = nx,ny
				break
		if part2:
			if (xs,ys) == (500,0):
				plane[(xs,ys)] = 'o'
				stop_flow = True
				break
			if (xs,ys) not in ns or ys == max_y + 1:
				plane[(xs,ys)] = 'o'
				break
		else:
			if ys > max_y:
				stop_flow = True
				break
			if (xs,ys) not in ns:
				plane[(xs,ys)] = 'o'
				break

res = 0
for x,y in plane:
	if plane[(x,y)] == 'o':
		res += 1

print(f"Part {2 if part2 else 1}: {res}")
