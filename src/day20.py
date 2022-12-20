#!/usr/bin/python3

f = open("../data/day20.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [int(x) for x in input_data.split('\n') if x != '']

class Node:
	def __init__(self, v):
		self.val = v
		self.next = self
		self.prev = self
	def append(self,node):
		node.prev = self
		self.next.prev = node
		node.next = self.next
		self.next = node
		return node
	def move(self):
		n = self.val
		if n == 0:
			return
		n = n % (len(data)-1)

		dest = self
		for _ in range(n+1):
			dest = dest.next
		prev_dest = dest.prev
		prev_n = self.prev
		next_n = self.next
		prev_n.next = next_n
		next_n.prev = prev_n
		prev_dest.next = self
		self.prev = prev_dest
		self.next = dest
		dest.prev = self

last_node = None

node_refs = []

for d in data:
	if part2:
		d *= 811589153
	if not last_node:
		last_node = Node(d)
		node_refs.append(last_node)
	else:
		n = Node(d)
		last_node = last_node.append(n)
		assert last_node == n
		node_refs.append(n)
		if d == 0:
			zero_node = n

for _ in range(10 if part2 else 1):
	for i in range(len(node_refs)):
		node_refs[i].move()

res = 0
n = zero_node

for x in range(3):
	for i in range(1000):
		n = n.next
	res += n.val

print(f"Part {2 if part2 else 1}: {res}")
