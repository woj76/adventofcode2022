#!/usr/bin/python3

import requests
import os

session_cookie = { 'session' : 'deadbeef'}

def get_input():
	url = f"https://adventofcode.com/{year}/day/{day}/input"
	fn = f"day{day}.txt"
	if not os.path.exists(fn):
		r = requests.get(url, headers={'Cache-Control': 'no-cache'}, cookies=session_cookie)
		f = open(fn, "wt")
		f.write(r.text)
		f.close()
	f = open(fn, "rt")
	r = f.read()
	f.close()
	print(r)
	return r

def repres(ans):
	stamp_file = f"day{day}level1.txt"
	if os.path.exists(stamp_file):
		lvl = 2
	else:
		lvl = 1
	url = f"https://adventofcode.com/{year}/day/{day}/answer"
	r = requests.post(url, cookies=session_cookie, data={ 'level' : lvl, 'answer' : ans})
	r = r.text
	correct = ("That's the right answer!" in r)
	if correct:
		f = open(stamp_file, "wt")
		f.write("Yes!\n")
		f.close()
	print("Correct: "+("YES" if correct else "NO"))

year = 2022
day = 21

input_data = get_input()
# input_data = open(f"day{day}test.txt", "rt").read()

data = [x for x in input_data.split('\n') if x != '']

part2 = os.path.exists(f"day{day}level1.txt")

monkeys = {}

for d in data:
	d = d.split(': ')
	ops = d[1].split(' ')
	if len(ops) == 3:
		monkeys[d[0]] = (ops[0],ops[1],ops[2])
	else:
		monkeys[d[0]] = int(ops[0])

# print(monkeys)

results = {}

def eval(monkey):
	if monkey in results:
		return results[mokey]
	if type(monkeys[monkey]) == int:
		results[monkey] = monkeys[monkey]
		return monkeys[monkey]
	m1,op,m2 = monkeys[monkey]
	r1 = eval(m1)
	r2 = eval(m2)
	if op == '+':
		r = r1 + r2
	elif op == '-':
		r = r1 - r2
	elif op == '*':
		r = r1 * r2
	elif op == '/':
		r = r1 / r2
	results[monkey] = r
	return r

def eval2(monkey,target):
	if type(monkeys[monkey]) == int:
		if monkey == 'humn' and target:
			monkeys[monkey] = target
		return monkey=='humn', monkeys[monkey]
	m1,op,m2 = monkeys[monkey]
	h1,r1 = eval2(m1,None)
	h2,r2 = eval2(m2,None)
	if op == '=':
		if h1:
			h1,r1 = eval2(m1,r2)
		elif h2:
			h2,r2 = eval2(m2,r1)
		r = "Equal"
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

monkeys['root'] = (monkeys['root'][0],'=',monkeys['root'][2])


res = eval2('root',None)
res = monkeys['humn']


print(f"Part X: {res}")
#repres(res)
