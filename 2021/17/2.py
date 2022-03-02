f = open("input.txt", "r")
data = f.read().split('=')

target_y = data[1][:data[1].find(',')].split('..')
target_x = data[2].split('..')


class Probe:
	velocity = []
	position = []

	def __init__(self, initial_velocity):
		self.velocity = initial_velocity
		self.position = [0, 0]

	def is_in_target(self):
		x, y = self.position
		if not int(target_x[0]) <= x <= int(target_x[1]):
			return False
		if not int(target_y[0]) <= y <= int(target_y[1]):
			return False
		return True

	def is_over_target(self):
		x, y = self.position
		if x < int(target_x[0]):
			return True
		if y > int(target_y[1]):
			return True
		return False


	def tick(self):
		self.position[0] += self.velocity[0]
		self.position[1] += self.velocity[1]
		self.velocity[0] -= 1
		self.velocity[1] = max(self.velocity[1] - 1, 0)




counter = 0
for vel_y in range(int(target_y[1])+1):
	for vel_x in range(-100, 100):
		probe = Probe([vel_x, vel_y])

		local_highest_value = 0
		while True:
			probe.tick()

			if probe.is_in_target():
				counter += 1
				break
			if probe.is_over_target():
				break

print(counter)