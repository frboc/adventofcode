

f = open("input.txt", "r")
data_raw = f.read()
data = data_raw.split('\n')

MAP1 = ['[', '{', '(', '<']
MAP2 = [']', '}', ')', '>']

def get_stack(row):
	stack = []
	for ch in row:
		if ch in MAP1:
			stack.append(ch)
		elif MAP1.index(stack.pop()) == MAP2.index(ch):
			pass
		else:
			return False
	return stack


completed = []
for row in data:
	stack = get_stack(row)

	if not stack:
		continue

	completed.append([])
	while stack:
		if len(stack) == 0:
			break
		ch = stack.pop()
		i = MAP1.index(ch)
		completed[-1].append(MAP2[i])


POINTS = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4
}

sum_arr = []
for x in completed:
	sum = 0
	for ch in x:
		sum *= 5
		sum += POINTS[ch]
	sum_arr.append(sum)

sum_arr.sort()

print(sum_arr[len(sum_arr)//2])

