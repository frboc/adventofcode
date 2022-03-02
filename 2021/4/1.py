f = open("input.txt", "r")
raw_data = f.read()
data = raw_data.split("\n")

numbers = data[0].split(',')
boards = []

for i, row in enumerate(data[2:]):
	if (row == ''):
		continue
	board_index = i // 6
	if (i % 6 == 0):
		boards.insert(board_index, [])
	row_final = list(filter(lambda x: x != '', row.split(' ')))
	boards[board_index].append(row_final)

win_board = [[[0]*5 for i in range(5)] for x in range(len(boards))]


def mark_number(board, win_board, number):
	for x in range(5):
		for y in range(5):
			if number == board[x][y]:
				win_board[x][y] = 1


def is_winner(board, win_board):
	for x in range(5):
		if win_board[x] == [1, 1, 1, 1, 1]:
			return True

	for x in range(5):
		column_win = []
		for y in range(5):
			column_win.append(win_board[y][x])
		if column_win == [1, 1, 1, 1, 1]:
			return True
	return False

def count_magic_number(board, winning_numbers):
	sum = 0
	for x in range(5):
		for y in range(5):
			if (not board[x][y] in winning_numbers):
				sum += int(board[x][y])
	return sum * int(winning_numbers[-1])

winning_numbers = []
for number in numbers:
	winning_numbers.append(number)

	for i in range(len(boards)):
		mark_number(boards[i], win_board[i], number)
		if (is_winner(boards[i], win_board[i])):
			print(count_magic_number(boards[i], winning_numbers))
			exit()


exit()

for board in win_board:
	print('board')
	for row in board:
		print(row)
for board in boards:
	print('board')
	for row in board:
		print(row)
		