from collections import defaultdict

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


def is_valid(ticket):
	not_valid = []
	for number in ticket:
		valid = False
		for _, rule1, rule2 in rules:
			if rule1[0] <= number <= rule1[1] or rule2[0] <= number <= rule2[1]:
				valid = True
				break
		if not valid:
			not_valid.append(number)

	return not_valid == []


def get_rule(column, used_rules):
	possible = []
	for rule_name, rule1, rule2 in rules:
		if rule_name in used_rules.values():
			continue

		valid_rule = True
		for number in column:
			if (rule1[0] <= number <= rule1[1] or rule2[0] <= number <= rule2[1]):
				pass
			else:
				valid_rule = False
				break
		if valid_rule:
			possible.append(rule_name)

	if len(possible) == 1:
		return possible[0]


valid_tickets = []
for ticket in nearby_tickets:
	if is_valid(ticket):
		valid_tickets.append(ticket)


columns = []
for i in range(len(nearby_tickets[0])):
	columns.append([])
	for ticket in valid_tickets:
		columns[-1].append(ticket[i])

columns_finished = {}
rules_order = {}
while len(columns) != len(columns_finished):
	for i, column in enumerate(columns):
		rule = get_rule(column, rules_order)

		if rule:
			rules_order[i] = rule
			columns_finished[i] = True
			break



res = 1
for i in range(len(my_ticket)):
	rule = rules_order[i]
	if rule and rule[:9] == 'departure':
		res *= my_ticket[i]

print(res)
assert res == 1265347500049