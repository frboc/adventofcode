
data = open("input.txt", "r").read().split("\n")

# E, N
position_w = [10, 1]
position = [0, 0]

def transform_w(tick_right):
	global position_w
	#0 = [1, 2]
	#90 = [2, -1]
	#180 [-1, -2]
	#270 [-2, 1]
	for _ in range(tick_right):
		position_w = [position_w[1], position_w[0]*-1]


for instruction in data:
	if instruction[0] == 'F':
		for i in range(int(instruction[1:])):
			position[0] += position_w[0]
			position[1] += position_w[1]
	if instruction[0] == 'N':
		position_w[1] += int(instruction[1:])
	if instruction[0] == 'S':
		position_w[1] -= int(instruction[1:])
	if instruction[0] == 'E':
		position_w[0] += int(instruction[1:])
	if instruction[0] == 'W':
		position_w[0] -= int(instruction[1:])
	if instruction[0] == 'L':
		transform_w(4 - int(instruction[1:]) // 90)
	if instruction[0] == 'R':
		transform_w(int(instruction[1:]) // 90)
	# print(position, position_w, instruction)


print(position_w)
result = abs(position[0]) + abs(position[1])
print(result)
assert result == 39140