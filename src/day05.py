#!/usr/bin/python3

from collections import deque

f = open("../data/day05.txt","rt")
input_data = f.read()
f.close()

part2 = True

[stacks,moves] = input_data.split('\n\n')

stacks = stacks.split('\n')
stacks.reverse()

num_stacks = len(stacks[0].split('   '))
stacks = stacks[1:]

piles = []
for i in range(num_stacks):
	piles.append(deque())

for sl in stacks:
	for i in range(num_stacks):
		c = sl[i*4+1]
		if c != ' ':
			piles[i].append(c)

moves = [x.split(' ') for x in moves.split('\n') if x != '']

for m in moves:
	l,f,t = int(m[1]),int(m[3])-1,int(m[5])-1
	if part2:
		tmp = deque()
		for i in range(l):
			e = piles[f].pop()
			tmp.append(e)
		for i in range(l):
			e = tmp.pop()
			piles[t].append(e)
	else:
		for i in range(l):
			piles[t].append(piles[f].pop())

print("".join([p[-1] for p in piles]))
