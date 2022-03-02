data = list(map(int, open("input.txt", "r").read().split("\n")))

def is_valid(numbers, goal):
	for i in numbers:
		for j in numbers:
			if i + j == goal:
				return True
	return False

def do_magic(goal):
	for i, _ in enumerate(data):
		for j, _ in enumerate(data):
			total = sum(data[i:j])
			if total == goal:
				return data[i:j]
			if total > goal:
				break


goal = 0
for i in range(len(data)):
	if i < 25:
		continue

	result = is_valid(data[i-25:i], data[i])
	if not result:
		goal = data[i]
		break




resultN = do_magic(goal)
result = min(resultN) + max(resultN)

print(result)
assert result == 20532569