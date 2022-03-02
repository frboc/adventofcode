data = []
mask = ''
for row in open("input.txt", "r").read().split("\n"):
	if row[:4] == 'mask':
		data.append((row.split(' = ')[1], []))
	else:
		memory, value = row.split(' = ')
		data[-1][1].append((''.join(filter(str.isdigit, memory)), int(value)))


def get_addresses(number, mask):
	number = list(format(int(number), 'b').zfill(36))
	for i in range(1, len(mask)+1):
		if mask[-i] == "0":
			continue
		number[-i] = '1' if mask[-i] == '1' else "X"

	paths = [number]
	res = []
	while paths:
		path = paths.pop(0)
		if not "X" in path:
			res.append(path)
			continue
		for i, ch in enumerate(path):
			if not ch == 'X':
				continue
			path[i] = '0'
			paths.append(path.copy())
			path[i] = '1'
			paths.append(path.copy())

	res_int = []
	for num in res:
		res_int.append(int("".join(num), 2))

	return set(res_int)


memory = {}
for mask, numbers in data:
	for number in numbers:
		adresses = get_addresses(number[0], mask)

		for adress in adresses:
			memory[adress] = number[1]



result = 0
for val in memory.values():
	result += val

print(result)
assert result == 3706820676200