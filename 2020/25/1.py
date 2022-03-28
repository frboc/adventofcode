a, b = list(map(int, open("input.txt", "r").read().split('\n')))
# a, b = 5764801, 17807724



def get_loop_size(starting_number, result_number):
	number = 1
	i = 1
	MEMO = {}
	while True:
		number *= starting_number
		number %= 20201227

		if number in MEMO:
			return None
		MEMO[number] = True


		if number == result_number:
			return i
		i += 1


def loop(times, starting_number):
	number = 1
	for _ in range(times):
		number *= starting_number
		number %= 20201227
	return number


def magic():
	i = 1
	for i in range(max(a, b,)):
		loop_size_a = get_loop_size(i, a)
		loop_size_b = get_loop_size(i, b)

		if loop_size_a and loop_size_b:
			return loop(loop_size_a, b)

		i += 1

result = magic()
print(result)
assert result == 4968512
