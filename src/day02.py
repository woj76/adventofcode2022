#!/usr/bin/python3

f = open("../data/day02.txt","rt")
input_data = f.read()
f.close()

data = [x.strip().replace(' ','') for x in input_data.split('\n') if x != '']

part2 = True

scores ={}
scores['AX'] = 3+1
scores['AY'] = 6+2
scores['AZ'] = 0+3
scores['BX'] = 0+1
scores['BY'] = 3+2
scores['BZ'] = 6+3
scores['CX'] = 6+1
scores['CY'] = 0+2
scores['CZ'] = 3+3

p2 = {}
p2['AX'] = 'AZ'
p2['AY'] = 'AX'
p2['AZ'] = 'AY'
p2['BX'] = 'BX'
p2['BY'] = 'BY'
p2['BZ'] = 'BZ'
p2['CX'] = 'CY'
p2['CY'] = 'CZ'
p2['CZ'] = 'CX'

res = 0

for d in data:
	if part2:
		d = p2[d]
	res += scores[d]

print(res)
