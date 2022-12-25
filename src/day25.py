#!/usr/bin/python3

f = open("../data/day25.txt", "rt")
input_data = f.read()
f.close()

data = [x for x in input_data.split('\n') if x != '']

from_snafu = {'0':0,'1':1,'2':2,'-':-1,'=':-2}
to_snafu = {0:('0',0),1:('1',0),2:('2',0),3:('=',1),4:('-',1)}

sum = 0

for d in data:
	d = reversed(d)
	num = 0
	base = 1
	for c in d:
		num += base*from_snafu[c]
		base *= 5
	sum += num

res = ""

while sum > 0:
	n1 = sum // 5
	n2 = sum % 5
	c,t = to_snafu[n2]
	n1 += t
	res = c+res
	sum = n1

print(f"Part 1: {res}")
