data = []
mask = ''
for row in open("input.txt", "r").read().split("\n"):
	if row[:4] == 'mask':
		data.append((row.split(' = ')[1], []))
	else:
		memory, value = row.split(' = ')
		data[-1][1].append((''.join(filter(str.isdigit, memory)), int(value)))


def do_magic(number, mask):
	number = list(format(number, 'b').zfill(36))
	for i in range(1, len(mask)+1):
		if mask[-i] == 'X':
			continue
		number[-i] = mask[-i]
	return int(''.join(number), 2)


memory = {}
for mask, numbers in data:
	for number in numbers:
		memory[number[0]] = do_magic(number[1], mask)



result = 0
for val in memory.values():
	result += val

print(result)
assert result == 14925946402938