#!/usr/bin/python3

f = open("../data/day04.txt","rt")
input_data = f.read()
f.close()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

res = 0

for d in data:
	[r1,r2] = d.split(',')
	r1 = [int(x) for x in r1.split('-')]
	r2 = [int(x) for x in r2.split('-')]
	if (r1[0] >= r2[0] and r1[1] <= r2[1]) or (r2[0] >= r1[0] and r2[1] <= r1[1]):
		res += 1
	elif part2:
		if (r1[0] >= r2[0] and r1[0] <= r2[1]) or (r1[1] >= r2[0] and r1[1] <= r2[1]):
			res += 1

print(res)
