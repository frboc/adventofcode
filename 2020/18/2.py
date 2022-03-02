from collections import deque

data = open("test_input.txt", "r").read().split("\n")

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
	parsed = expression.split(' ')

	while len(parsed) != 1:
		for i in range(len(parsed)):

			if parsed[i].startswith('('):
				parentesis = get_parentesis(" ".join(parsed))
				parentesis_len = len(parentesis.split(' '))
				for j in range(parentesis_len-1):
					parsed.pop(i)
				if i >= len(parsed):
					parsed.append(calc(parentesis))
				else:
					parsed[i] = calc(parentesis)

			print(parsed)
			i += 2
			if parsed[i].startswith('('):
				parentesis = get_parentesis(" ".join(parsed))
				parentesis_len = len(parentesis.split(' '))
				for j in range(parentesis_len-1):
					parsed.pop(i)
				if i >= len(parsed):
					parsed.append(calc(parentesis))
				else:
					parsed[i] = calc(parentesis)
			i -= 2

			print(parsed)
			num1 = parsed[i]
			operator = parsed[i+1]
			num2 = parsed[i+2]

			parsed.pop(i)
			parsed.pop(i)

			res = eval(num1 + operator + num2)
			parsed[i] = res

	return parsed.pop()


sum = 0
for row in data:
	print(calc(row))

print(sum)