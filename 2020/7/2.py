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


def count_bags(bag):
	counter = 1
	for num, bag in RULES[bag]:
		counter += count_bags(bag) * int(num)
	return counter


result = count_bags('shiny gold') - 1
print(result)
assert result == 9569