#!/usr/bin/python3

f = open("../data/day10.txt","rt")
input_data = f.read().strip()
f.close()

data = [x for x in input_data.split('\n') if x != '']

res = 0

x = 1
c = 0

cycles = [20, 60, 100, 140, 180, 220]

print("Part 2:")

for d in data:
	if d == 'noop':
		c += 1
		cc = c % 40
		p = '#' if cc-2<=x<=cc else ' '
		print(p,end='')
		if c in cycles:
			res += (c * x)
		if c % 40 == 0:
			print()
	else:
		v = int(d.split()[1])
		for _ in range(2):
			c += 1
			cc = c % 40
			p = '#' if cc-2<=x<=cc else ' '
			print(p,end='')
			if c in cycles:
				res += (c * x)
			if c % 40 == 0:
				print()
		x += v

print(f"Part 1: {res}")
