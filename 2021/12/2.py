
f = open("input.txt", "r")
data_raw = f.read()
data = data_raw.split("\n")

map = []
for row in data:
	key, val = row.split('-')
	map.append((key, val))

def is_valid_small_cave(way):
	way = list(filter(lambda x: x.islower() and x != 'start', way))
	has_double_visit = False
	for i in range(len(way)):
		if way[i] in way[:i]:
			if has_double_visit:
				return False
			has_double_visit = True
	return True


def is_valid(way):
	if way in ways:
		return False
	if not is_valid_small_cave(way):
		return False
	if len(way) > 2 and way[-1] == 'start':
		return False
	return True

def get_ways(way):
	res = []
	for a, b in map:
		if a == way[-1] and is_valid(way + [b]):
			res.append(way + [b])
	for b, a in map:
		if a == way[-1] and is_valid(way + [b]):
			res.append(way + [b])
	return res

ways = [['start']]

win = []
while True:
	if len(ways)==0:
		break
	way = ways.pop()
	if way[-1] == 'end':
		win.append(way)
		continue
	ways += get_ways(way)


print(len(win))
