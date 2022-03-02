import itertools
import re

rules_raw, text = open("input.txt", "r").read().split('\n\n')

rules = {}
for rule in rules_raw.split('\n'):
	i, val = rule.split(': ')
	rules[i] = val

MAX_LEN = max(map(len, text.split('\n')))

rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

def get_text(rule_val):

	if rule_val.startswith('"'):
		return [rule_val.strip('"')]

	if '|' in rule_val:
		if rule_val == '42 | 42 8':
			x = '|'.join(get_text(rules['42']))
			x = ['(' + x + ')+']
			return x

		if rule_val == '42 31 | 42 11 31':
			res = []
			for i in range(1, 30):
				i = str(i)
				x = '|'.join(get_text(rules['42']))
				x = '(' + x + '){'+i+'}'
				y = '|'.join(get_text(rules['31']))
				y = '(' + y + '){'+i+'}'
				res.append(x + y)
			return res

		a, b = rule_val.split(' | ')
		res = get_text(a) + get_text(b)
		return res

	r = rule_val.split(' ')
	res = get_text(rules[r[0]])
	for rule_id in r[1:]:
		res = product(res, get_text(rules[rule_id]))

	return res

def product(x, y):
	if y == []:
		return x

	res = []
	for a in x:
		for b in y:
			res.append(a + b)
	return res


posibilities = get_text(rules['0'])

found = []
for posibility in posibilities:
	for line in text.split('\n'):
		pos = re.search('^'+posibility+'$', line)
		if (pos):
			a, b = pos.span()
			found.append(line)

res = len(set(found))
print(res)
assert res == 306