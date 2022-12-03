#!/usr/bin/python3

f = open("../data/day03.txt","rt")
input_data = f.read()
f.close()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

priors = {}

p = 1
for c in range(ord('a'), ord('z')+1):
	priors[chr(c)] = p
	p += 1
for c in range(ord('A'), ord('Z')+1):
	priors[chr(c)] = p
	p += 1

res = 0

i = 0
while i < len(data):
	if part2:
		d1, d2, d3 = data[i], data[i+1], data[i+2]
		for c in priors.keys():
			if c in d1 and c in d2 and c in d3:
				res += priors[c]
				break
		i += 3
	else:
		d = data[i]
		l = len(d) // 2
		first, second = d[:l], d[l:]
		for c in first:
			if c in second:
				res += priors[c]
				break
		i += 1

print(res)
