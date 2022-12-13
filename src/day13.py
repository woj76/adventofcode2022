#!/usr/bin/python3

from functools import cmp_to_key

f = open("../data/day13.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [x for x in input_data.split('\n\n') if x != '']

def compare(l1,l2):
	if type(l1) == int and type(l2) == int:
		return -1 if l1 < l2 else (1 if l1 > l2 else 0)
	if type(l1) == int:
		l1 = [l1]
	if type(l2) == int:
		l2 = [l2]
	i = 0
	while i < len(l1) or i < len(l2):
		if i >= len(l1):
			return -1
		if i >= len(l2):
			return 1
		r = compare(l1[i],l2[i])
		if r != 0:
			return r
		i += 1
	return 0

if part2:
	packets = []
	for d in data:
		packets.extend([eval(x) for x in d.split('\n')])
	dividers = [[[2]],[[6]]]
	packets.extend(dividers)
	packets.sort(key = cmp_to_key(compare))
	res = 1
	index = 1
	for p in packets:
		if p in dividers:
			res *= index
		index += 1
else:
	res = 0
	index = 1
	for d in data:
		[l1,l2] = [eval(x) for x in d.split('\n')]
		if compare(l1,l2) == -1:
			res += index
		index += 1

print(f"Part {2 if part2 else 1}: {res}")
