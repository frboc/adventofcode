f = open("input.txt", "r")
raw_data = f.read()
data = raw_data.split("\n")


def magic(line):
	input, out = line.split(' | ')
	out = out.split(' ');
	counter = 0

	for o in out:
		if (len(o) in [2, 4, 3, 7]):
			counter += 1

	return counter


counter = 0
for line in data:
	counter += magic(line)

print(counter)