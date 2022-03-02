data = open("input.txt", "r").read().split("\n")


RULES = {}
for row in data:
	rule_name, inside = row.split(' bags contain')
	RULES[rule_name] = []
	for bag_inside in inside.strip().split(','):
		if (bag_inside == 'no other bags.'):
			continue
		number, name1, name2, rest = bag_inside.split()
		RULES[rule_name].append((number, name1 + ' ' +name2))


def has_gold(bag):
	for num, bag in RULES[bag]:
		if bag == 'shiny gold':
			return True
		if has_gold(bag):
			return True
	return False


counter = 0
for rule_name in RULES:
	if has_gold(rule_name):
		counter += 1


print(counter)
assert counter == 226