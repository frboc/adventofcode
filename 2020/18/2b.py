from collections import deque

data = open("input.txt", "r").read().split("\n")

def get_parentesis(expression):
	stack = []
	start = expression.index('(')
	for i, ch in enumerate(expression):
		if i < start:
			continue
		if ch == '(':
			stack.append(ch)
		if ch == ')':
			stack.pop(0)
		if stack == []:
			return expression[start+1:i]
	raise Exception('asdf')


def calc(expression):
	parsed = deque(expression.split(' '))

	while len(parsed) != 1:
		if parsed[0].startswith('('):
			parentesis = get_parentesis(" ".join(parsed))
			parentesis_len = len(parentesis.split(' '))
			for i in range(parentesis_len):
				parsed.popleft()
			parsed.appendleft(calc(parentesis))
			continue

		if parsed[2].startswith('('):
			parentesis = get_parentesis(" ".join(parsed))
			parentesis_len = len(parentesis.split(' '))
			num1 = parsed.popleft()
			operator = parsed.popleft()
			for i in range(parentesis_len):
				parsed.popleft()
			parsed.appendleft(calc(parentesis))
			parsed.appendleft(operator)
			parsed.appendleft(num1)
			continue

		if parsed[1] == '*' and parsed.count('+') > 0:
			num1 = parsed.popleft()
			operator = parsed.popleft()
			num2 = parsed.popleft()
			parsed.appendleft('(' + num2)
			parsed.appendleft(operator)
			parsed.appendleft(num1)
			last = parsed.pop()
			parsed.append(last + ')')
			continue


		num1 = parsed.popleft()
		operator = parsed.popleft()
		num2 = parsed.popleft()

		res = eval(num1 + operator + num2)
		parsed.appendleft(str(res))

	return parsed.pop()


sum = 0
for row in data:
	sum += int(calc(row))

print(sum)
assert sum == 141993988282687