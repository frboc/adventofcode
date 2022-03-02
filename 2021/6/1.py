f = open("test_input.txt", "r")
raw_data = f.read()
data = raw_data.split(",")

class Fish:
	time = 0

	def __init__(self, time):
		self.time = time

	def __str__(self):
		return str(self.time)

	def tick(self):
		if (self.time == 0):
			self.time = 6
			return Fish(9)
		else:
			self.time -= 1

school = []
for i in data:
	school.append(Fish(int(i)))

for i in range(10):
	for fish in school:
		new_fish = fish.tick()
		if new_fish:
			school.append(new_fish)
	

print(len(school))
