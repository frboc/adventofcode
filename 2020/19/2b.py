import itertools

rules_raw, asdf = open("test_input.txt", "r").read().split('\n\n')

MAX_LEN = 45

rules = {}
for rule in rules_raw.split('\n'):
	i, val = rule.split(': ')
	rules[int(i)] = val

def get_matching_text(rule_val, text):
	if rule_val.startswith('"'):
		ch = rule_val.strip('"')
		if text.startswith(ch):
			return text[len(ch):]
		return False

	if '|' in rule_val:
		a, b = rule_val.split(' | ')
		t = get_matching_text(rules[int(a)], text)
		print(t)
		if t:
			return text[len(t):]
		t = get_matching_text(rules[int(b)], text)
		print(t)
		if t:
			return text[len(t):]
		return False

	r = list(map(int, rule_val.split(' ')))
	for rule_id in r:
		text = get_matching_text(rules[rule_id], text)
		if text == False:
			return False

	if text == '':
		return ''

	return text

print(get_matching_text('14 | 1', 'baaa'))