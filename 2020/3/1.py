f = open("input.txt", "r")
data = f.read().split("\n")

X = len(data)
Y = len(data[0])
pos = [0, 0]
counter = 0
while True:
	pos = [pos[0]+1, pos[1]+3]
	a, b = pos
	if data[a][b % Y] == "#":
		counter += 1
	if a >= X-1:
		break
		

print(counter)
assert counter == 225