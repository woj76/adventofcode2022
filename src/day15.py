#!/usr/bin/python3

f = open("../data/day15.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [x for x in input_data.split('\n') if x != '']

coords = []

for d in data:
	d = d.split(': ')
	s = d[0][10:]
	b = d[1][21:]
	s = s.split(', ')
	b = b.split(', ')
	r = [(int(s[0][2:]),int(s[1][2:])),(int(b[0][2:]),int(b[1][2:]))]
	[(sx,sy),(bx,by)] = r
	r.append(abs(bx-sx)+abs(by-sy))
	coords.append(r)

for ry in (range(4000001) if part2 else [2000000]):
	xs = []
	for s in coords:
		sx,sy = s[0]
		r = s[2]
		if sy-r<=ry<=sy+r:
			rx = r - abs(ry - sy)
			xs.append((sx-rx,sx+rx))

	deleted = True
	while deleted:
		deleted = False
		for i in range(len(xs)):
			for j in range(i+1,len(xs)):
				x1,x2 = xs[i]
				xx1,xx2 = xs[j]
				if x1 >= xx1 and x2 <= xx2:
					del xs[i]
					deleted = True
					break
				if xx1 >= x1 and xx2 <= x2:
					del xs[j]
					deleted = True
					break
				if xx1 <= x1 <= xx2:
					assert x2 > xx2
					xs[j] = (xx1,x2)
					del xs[i]
					deleted = True
					break
				if xx1 <= x2 <= xx2:
					assert x1 < xx1
					xs[j] = (x1,xx2)
					del xs[i]
					deleted = True
					break
				if x1 <= xx1 <= x2:
					assert xx2 > x2
					xs[i] = (x1,xx2)
					del xs[j]
					deleted = True
					break
				if x1 <= xx2 <= x2:
					assert xx1 < x1
					xs[i] = (xx1,x2)
					del xs[j]
					deleted = True
					break
			if deleted:
				break
	if part2 and len(xs) > 1:
		break

if part2:
	xs.sort()
	res = 4000000*(xs[0][1]+1)+ry
else:
	res = (xs[0][1]-xs[0][0]) + 1
	ybs = {}

	for s in coords:
		bx,by = s[1]
		if by == ry:
			ybs[(bx,by)] = True
	res -= len(ybs)

print(f"Part {2 if part2 else 1}: {res}")
