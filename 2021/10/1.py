

f = open("input.txt", "r")
data_raw = f.read()
data = data_raw.split('\n')

MAP1 = ['[', '{', '(', '<']
MAP2 = [']', '}', ')', '>']

ilegal_characters = []
for row in data:
	stack = []
	for ch in row:
		if ch in MAP1:
			stack.append(ch)
		elif MAP1.index(stack.pop()) == MAP2.index(ch):
			pass
		else:
			ilegal_characters.append(ch)
			break

POINTS = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

sum = 0
for x in ilegal_characters:
	sum += POINTS[x]

print(sum)

