
data = open("input.txt", "r").read().split("\n")

# E, N
position = [0, 0]
facing = 90


for instruction in data:
	if instruction[0] == 'F':
		if facing == 0:
			position[1] += int(instruction[1:])
		if facing == 180:
			position[1] -= int(instruction[1:])
		if facing == 90:
			position[0] += int(instruction[1:])
		if facing == 270:
			position[0] -= int(instruction[1:])
	if instruction[0] == 'N':
		position[1] += int(instruction[1:])
	if instruction[0] == 'S':
		position[1] -= int(instruction[1:])
	if instruction[0] == 'E':
		position[0] += int(instruction[1:])
	if instruction[0] == 'W':
		position[0] -= int(instruction[1:])
	if instruction[0] == 'L':
		facing -= int(instruction[1:])
		facing = facing % 360
	if instruction[0] == 'R':
		facing += int(instruction[1:])
		facing = facing % 360

result = abs(position[0]) + abs(position[1])
print(result)
assert result == 858