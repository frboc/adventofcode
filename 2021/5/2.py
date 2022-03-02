f = open("input.txt", "r")
raw_data = f.read()
data = raw_data.split("\n")


class line:
	a, b, c, d = 0,0,0,0

	def __init__(self, raw_row):
		raw_row = raw_row.split(' -> ');
		self.a, self.b = list(map(int,raw_row[0].split(',')))
		self.c, self.d = list(map(int,raw_row[1].split(',')))

	def get_all_affected_points(self):
		res = [(self.a, self.b)]

		vector = [0, 0]
		if self.a > self.c:
			vector[0] = 1
		elif self.a < self.c:
			vector[0] = -1

		if self.b > self.d:
			vector[1] = 1
		elif self.b < self.d:
			vector[1] = -1
		
		steps = max(abs(self.a-self.c), abs(self.b-self.d))
		for i in range(steps):
			res.append((self.c+(vector[0]*i), self.d+(vector[1]*i)))
		return res


lines = []
for row in data:
	line_o = line(row)
	lines.append(line_o)

map = [[0] * 1000 for i in range(1000)]

for line in lines:
	for point in line.get_all_affected_points():
		map[point[1]][point[0]] += 1


for line in map:
	print(line)

res = 0
for row in map:
	for i in row:
		if i>=2:
			res +=1


print(res)

