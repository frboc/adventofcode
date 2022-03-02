f = open("input.txt", "r")
data = list(map(int, f.read().split("\n")))


for x in data:
	for y in data:
		if x + y == 2020:
			print(x * y)
			exit()