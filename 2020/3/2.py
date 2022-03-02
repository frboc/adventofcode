f = open("input.txt", "r")
data = f.read().split("\n")

X = len(data)
Y = len(data[0])

result = 1
for (c, d) in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
	pos = [0, 0]
	counter = 0
	while True:
		pos = [pos[0]+c, pos[1]+d]
		a, b = pos
		if data[a][b % Y] == "#":
			counter += 1
		if a >= X-1:
			break

	result *= counter

print(result)
assert result == 1115775000