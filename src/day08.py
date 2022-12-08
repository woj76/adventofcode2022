#!/usr/bin/python3

f = open("../data/day08.txt", "rt")
data = [[int(y) for y in list(x)] for x in f.read().split('\n') if x != '']
f.close()

x = len(data[0])
y = len(data)

res = 0

best_view = float('-inf')

for j in range(0,y):
	for i in range(0,x):
		smaller1 = True
		s1 = 0
		for k in range(i-1,-1,-1):
			s1 += 1
			if data[j][k] >= data[j][i]:
				smaller1 = False
				break
		smaller2 = True
		s2 = 0
		for k in range(i+1,x):
			s2 += 1
			if data[j][k] >= data[j][i]:
				smaller2 = False
				break
		smaller3 = True
		s3 = 0
		for k in range(j-1,-1,-1):
			s3 += 1
			if data[k][i] >= data[j][i]:
				smaller3 = False
				break
		smaller4 = True
		s4 = 0
		for k in range(j+1,y):
			s4 += 1
			if data[k][i] >= data[j][i]:
				smaller4 = False
				break
		if smaller1 or smaller2 or smaller3 or smaller4:
			res += 1
		best_view = max(best_view, s1 * s2 * s3 * s4)

print(f"Part 1: {res}")
print(f"Part 2: {best_view}")
