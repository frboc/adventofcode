import itertools

rules_raw, text = open("input.txt", "r").read().split('\n\n')

rules = {}
for rule in rules_raw.split('\n'):
	i, val = rule.split(': ')
	rules[i] = val




def get_text(rule_val):
	if rule_val.startswith('"'):
		return [rule_val.strip('"')]

	if '|' in rule_val:
		if len(rule_val.split(' ')) == 3:
			r1, _, r3 = rule_val.split(' ')
			res = []

			for v1 in get_text(rules[r1]):
				res.append(v1)
			for v3 in get_text(rules[r3]):
				res.append(v3)
			return res

		r1, r2, _, r3, r4 = rule_val.split(' ')
		res = []

		for v1 in get_text(rules[r1]):
			for v2 in get_text(rules[r2]):
				res.append(v1 + v2)

		for v3 in get_text(rules[r3]):
			for v4 in get_text(rules[r4]):
				res.append(v3 + v4)

		return res

	r = rule_val.split(' ')
	res = get_text(rules[r[0]])
	for rule_id in r[1:]:
		res = list(map(lambda x: "".join(x), itertools.product(res, get_text(rules[rule_id]))))
	return res



# print(get_text('4 | 5'))
# exit()

posibilities = get_text(rules['0'])

counter = 0
for row in text.split('\n'):
	if row in posibilities:
		counter += 1

print(counter)
assert counter == 132
