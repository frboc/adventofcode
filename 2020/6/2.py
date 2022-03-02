data = open("input.txt", "r").read().split("\n\n")



sum = 0
for group in data:
	persons = group.split('\n')
	common_chars = list(persons[0])

	for char in common_chars.copy():
		for person in persons:
			if not char in person and char in common_chars:
				common_chars.remove(char)

	print(common_chars, len(common_chars))
	sum += len(common_chars)

print(sum)
assert sum == 3579