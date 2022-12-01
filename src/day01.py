#!/usr/bin/python3

f = open("../data/day01.txt", "rt")
data = [x for x in f.read().split('\n\n') if x != '']
f.close()

part2 = True

food = []

for d in data:
	food.append(sum([int(x) for x in d.split('\n') if x != '']))

food.sort()

print(sum(food[len(food)-(3 if part2 else 1):]))
