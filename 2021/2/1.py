f = open("input.txt", "r")
raw_data = f.read()
data = raw_data.split("\n")

position_h = 0
position_v = 0

for command in data:
	direction, distance = command.split(' ');
	distance = int(distance)

	if direction == 'forward':
		position_h += distance
	if direction == 'down':
		position_v += distance
	if direction == 'up':
		position_v -= distance

print(position_v * position_h)