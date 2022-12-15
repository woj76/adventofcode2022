#!/snap/bin/pypy3

f = open("../data/day11.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [x for x in input_data.split('\n\n') if x != '']

monkey_items = []
monkey_ops = []
monkey_tests = []
monkey_pass = []

for d in data:
	d = d.split('\n')
	monkey_items.append([int(x) for x in d[1][18:].split(', ')])
	[op,val] = d[2][23:].split(' ')
	monkey_ops.append((op,val))
	monkey_tests.append(int(d[3][21:]))
	monkey_pass.append({True : int(d[4][29:]), 	False : int(d[5][30:])})

monkey_inspects = [0] * len(data)

all_p = 1
for p in monkey_tests:
	all_p *= p

round = 0
while round < (10000 if part2 else 20):
	for m in range(len(monkey_items)):
		for i in monkey_items[m]:
			monkey_inspects[m] += 1
			op,val = monkey_ops[m]
			v2 = i if val == 'old' else int(val)
			if op == '+':
				ni = i + v2
			elif op == '*':
				if part2:
					ni = (i * v2) % all_p
				else:
					ni = i * v2
			if not part2:
				ni = ni // 3
			test_result = (ni % monkey_tests[m] == 0)
			monkey_items[monkey_pass[m][test_result]].append(ni)
		monkey_items[m] = []
	round += 1

monkey_inspects.sort()
monkey_inspects.reverse()

print(f"Part {2 if part2 else 1}: {monkey_inspects[0] * monkey_inspects[1]}")
