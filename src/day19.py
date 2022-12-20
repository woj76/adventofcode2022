#!/usr/bin/python3

f = open("../data/day19.txt","rt")
input_data = f.read().strip()
f.close()

part2 = True

data = [x for x in input_data.split('\n') if x != '']

blueprints = {}

for d in data:
	d = d.split(' ')
	b_id = int(d[1][:-1])
	r_ore_cost = int(d[6])
	r_clay_cost = int(d[12])
	r_obsidian_cost = (int(d[18]),int(d[21]))
	r_goede_cost = (int(d[27]),int(d[30]))
	blueprints[b_id] = (r_ore_cost,r_clay_cost,r_obsidian_cost,r_goede_cost)

total_time = (32 if part2 else 24)

def search_max(blueprint,time,r_ore,r_clay,r_obsidian,r_goede,ore,clay,obsidian,goede):
	key = (time,r_ore,r_clay,r_obsidian,r_goede,ore,clay,obsidian,goede)
	rmax = -1
	if key in visited and visited[key] >= goede:
		return rmax
	else:
		visited[key] = goede
	if time == total_time:
		return goede
	time_left = total_time - time
	for make in [3,2,1,0]:
		cost = blueprint[make]
		if make == 0:
			if ore+r_ore*time_left >= max_ore*time_left:
				continue
			if ore >= cost:
				rmax = max(rmax,search_max(blueprint,time+1,r_ore+1,r_clay,r_obsidian,r_goede,ore-cost+r_ore,clay+r_clay,obsidian+r_obsidian,goede+r_goede))
			else:
				continue
		if make == 1:
			if clay+r_clay*time_left >= max_clay*time_left:
				continue
			if ore >= cost:
				rmax = max(rmax, search_max(blueprint,time+1,r_ore,r_clay+1,r_obsidian,r_goede,ore-cost+r_ore,clay+r_clay,obsidian+r_obsidian,goede+r_goede))
			else:
				continue
		if make == 2:
			if obsidian+r_obsidian*time_left >= max_obsidian*time_left:
				continue
			if ore >= cost[0] and clay >= cost[1]:
				rmax = max(rmax, search_max(blueprint,time+1,r_ore,r_clay,r_obsidian+1,r_goede,ore-cost[0]+r_ore,clay-cost[1]+r_clay,obsidian+r_obsidian,goede+r_goede))
			else:
				continue
		if make == 3:
			if ore >= cost[0] and obsidian >= cost[1]:
				return max(rmax, search_max(blueprint,time+1,r_ore,r_clay,r_obsidian,r_goede+1,ore-cost[0]+r_ore,clay+r_clay,obsidian-cost[1]+r_obsidian,goede+r_goede))
			else:
				continue
	return max(rmax, search_max(blueprint,time+1,r_ore,r_clay,r_obsidian,r_goede,ore+r_ore,clay+r_clay,obsidian+r_obsidian,goede+r_goede))

res = 1 if part2 else 0

for b in ([1,2,3] if part2 else blueprints):
	visited = {}
	bp = blueprints[b]
	max_ore = max(bp[0],bp[1],bp[2][0],bp[3][0])
	max_clay = bp[2][1]
	max_obsidian = bp[3][1]
	m = search_max(bp,0,1,0,0,0,0,0,0,0)
	if part2:
		res *= m
	else:
		res += b*m

print(f"Part {2 if part2 else 1}: {res}")
