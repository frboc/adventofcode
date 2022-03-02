data = list(map(int, open("input.txt", "r").read().split("\n")))

def is_valid(numbers, goal):
	for i in numbers:
		for j in numbers:
			if i + j == goal:
				return True
	return False


for i in range(len(data)):
	if i < 25:
		continue

	result = is_valid(data[i-25:i], data[i])
	if not result:
		print(data[i])
		assert data[i] == 144381670
		exit()