
data = open("input.txt", "r").read().split("\n\n")

rules = []
for row in data[0].split('\n'):
	name, rest = row.split(':')
	rule1, _, rule2 = rest.split()
	rules.append((name, list(map(int, rule1.split('-'))), list(map(int, rule2.split('-')))))

my_ticket = list(map(int, data[1].split('\n')[1].split(',')))


nearby_tickets = []
for row in data[2].split('\n')[1:]:
	nearby_tickets.append(list(map(int, row.split(','))))

def get_not_valid(ticket):
	not_valid = []
	for number in ticket:
		valid = False
		for _, rule1, rule2 in rules:
			if rule1[0] <= number <= rule1[1] or rule2[0] <= number <= rule2[1]:
				valid = True
				break
		if not valid:
			not_valid.append(number)

	return not_valid

counter = 0
for ticket in nearby_tickets:
	counter += sum(get_not_valid(ticket))

print(counter)
assert counter == 25984