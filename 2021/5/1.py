f = open("input.txt", "r")
raw_data = f.read()
data = raw_data.split("\n")


class line:
	a, b, c, d = 0,0,0,0
	valid = False

	def __init__(self, raw_row):
		raw_row = raw_row.split(' -> ');
		self.a, self.b = list(map(int,raw_row[0].split(',')))
		self.c, self.d = list(map(int,raw_row[1].split(',')))

		if (self.a == self.c or self.b == self.d):
			self.valid = True

	def get_all_affected_points(self):
		res = [(self.a, self.b)]
		if self.b == self.d:
			vector = 1 if self.a > self.c else -1
			for i in range(abs(self.a-self.c)):
				res.append((self.c+(vector*i), self.b))

		if self.a == self.c:
			vector = 1 if self.b > self.d else -1
			for i in range(abs(self.b-self.d)):
				res.append((self.c, self.d+(vector*i)))

		return res


lines = []
for row in data:
	line_o = line(row)
	if line_o.valid:
		lines.append(line_o)

map = [[0] * 1000 for i in range(1000)]

for line in lines:
	for point in line.get_all_affected_points():
		map[point[1]][point[0]] += 1

res = 0
for row in map:
	for i in row:
		if i>=2:
			res +=1

print(res)

