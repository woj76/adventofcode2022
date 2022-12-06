#!/usr/bin/python3

f = open("../data/day06.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

l = 14 if part2 else 4

for i in range(l,len(input_data)):
	if len(set(list(input_data[i-l:i]))) == l:
		break

print(i)
