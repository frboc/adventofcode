f = open("input.txt", "r")
raw_data = f.read()
data = raw_data.split("\n")

position_h = 0
position_v = 0
aim = 0

for command in data:
	direction, unit = command.split(' ');
	unit = int(unit)

	if direction == 'forward':
		position_h += unit
		position_v += aim * unit
	if direction == 'down':
		aim += unit
	if direction == 'up':
		aim -= unit

print(position_v * position_h)