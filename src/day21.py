#!/usr/bin/python3

f = open("../data/day21.txt", "rt")
input_data = f.read()
f.close()

data = [x for x in input_data.split('\n') if x != '']

part2 = True

monkeys = {}

for d in data:
	d = d.split(': ')
	ops = d[1].split(' ')
	if len(ops) == 3:
		monkeys[d[0]] = (ops[0],ops[1],ops[2])
	else:
		monkeys[d[0]] = int(ops[0])

def eval2(monkey,target):
	if type(monkeys[monkey]) == int:
		if monkey == 'humn' and target:
			monkeys[monkey] = target
		return monkey=='humn', monkeys[monkey]
	m1,op,m2 = monkeys[monkey]
	h1,r1 = eval2(m1, None)
	h2,r2 = eval2(m2, None)
	if op == '=':
		if h1:
			h1,r1 = eval2(m1,r2)
		elif h2:
			h2,r2 = eval2(m2,r1)
		r = "="
	elif op == '+':
		if target:
			if h1:
				h1,r1 = eval2(m1,target-r2)
			elif h2:
				h2,r2 = eval2(m2,target-r1)
		r = r1 + r2
	elif op == '-':
		if target:
			if h1:
				h1,r1 = eval2(m1,target+r2)
			elif h2:
				h2,r2 = eval2(m2,r1-target)
		r = r1 - r2
	elif op == '*':
		if target:
			if h1:
				h1,r1 = eval2(m1,target//r2)
			elif h2 and target:
				h2,r2 = eval2(m2,target//r1)
		r = r1 * r2
	elif op == '/':
		if target:
			if h1 and target:
				h1,r1 = eval2(m1,target*r2)
			elif h2 and target:
				h2,r2 = eval2(m2,target*r1)
		r = r1 // r2
	return h1 or h2, r

if part2:
	monkeys['root'] = (monkeys['root'][0],'=',monkeys['root'][2])

_,res = eval2('root', None)
if part2:
	res = monkeys['humn']

print(f"Part {2 if part2 else 1}: {res}")
