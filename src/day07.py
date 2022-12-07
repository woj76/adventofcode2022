#!/usr/bin/python3

f = open("../data/day07.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = input_data.split('\n')

class Dir:
	def __init__(self,p):
		self.parent = p
		self.files = {}
		self.dirs = {}

root = Dir(None)

current = None

for d in data:
	if d[0] == '$':
		cmd = d[2:4]
		if cmd == 'cd':
			dir_name = d[5:]
			if dir_name == '/':
				current = root
			elif dir_name == '..':
				current = current.parent
			else:
				current = current.dirs[dir_name]
		else:
			assert cmd == 'ls'
	else:
		[sd,n] = d.split(' ')
		if sd == 'dir':
			nd = Dir(current)
			current.dirs[n] = nd
		else:
			sd = int(sd)
			current.files[n] = sd

sizes = {}

def size(cd,p):
	s = 0
	for d in cd.dirs:
		s += size(cd.dirs[d],p+d+"/")
	s += sum(cd.files.values())
	sizes[p] = s
	return s

size(root,"/")

if part2:
	res = min([s for s in sizes.values() if s + 40000000 >= sizes["/"]])
else:
	res = sum([s for s in sizes.values() if s <= 100000])

print(res)
