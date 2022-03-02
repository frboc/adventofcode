f = open("input.txt", "r")
data = list(map(int, f.read().split("\n")))


for x in data:
	for y in data:
		for z in data:
			if x + y + z == 2020:
				print(x * y * z)
				exit()