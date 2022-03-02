import copy
from collections import deque
from functools import reduce
import heapq

f = open("input.txt", "r")
data = f.read().split("\n")
board = []
for row in data:
	board.append(list(row))


def is_finish(board):
	if board[2][3] == 'A' and board[3][3] == 'A':
		if board[2][5] == 'B' and board[3][5] == 'B':
			if board[2][7] == 'C' and board[3][7] == 'C':
				if board[2][9] == 'D' and board[3][9] == 'D':
					return True
	return False

COST_MAP = {
	'A': 1,
	'B': 10,
	'C': 100,
	'D': 1000,
}

def do_move(board, ax, ay, bx, by):
	cost = abs(ax - bx) + abs(ay - by)
	cost *= COST_MAP[board[ax][ay]]

	board[bx][by] = board[ax][ay]
	board[ax][ay] = '.'
	return cost, board


def plot(board):
	for row in board:
		print("".join(row))


def get_moves_from_pos(board, x, y, moves = []):
	for i, j in [(0, 1),(1, 0),(0, -1),(-1, 0)]:
		try:
			if board[x+i][y+j] != '.':
				continue
			point = (x+i, y+j)
			#print(board[x+i][y+j], point)
			if point not in moves:
				moves.append(point)
				for move in get_moves_from_pos(board, *point, moves):
					if move not in moves:
						moves.append(move)
		except IndexError:
			pass

	return moves


def get_all_moves(board):
	moves = []
	for i in range(1,4):
		for j in range(1,12):
			try:
				if not board[i][j] in ['A', 'B', 'C', 'D']:
					continue

				valid = True
				for z, ch in zip([3,5,7,9], ['A','B','C','D']):
					if i == 2 and j == z and board[2][z] == ch and board[3][z] == ch:
						valid = False
					if i == 3 and j == z and board[3][z] == ch:
						valid = False
				if not valid:
					continue

				for move in filter_invalid_moves(board, i, j, get_moves_from_pos(board, i, j, [])):
					moves.append((i, j, *move))
			except IndexError:
				pass
	return moves


def filter_invalid_moves(board, x, y, moves):
	filtered = []
	for move in moves:
		if move == (x, y):
			continue
		if move in [(1,3),(1,5),(1,7),(1,9)]:
			continue

		if x == 1:
			if move[0] == 1:
				continue
			if board[x][y] == 'A' and move[1] != 3:
				continue
			if board[x][y] == 'B' and move[1] != 5:
				continue
			if board[x][y] == 'C' and move[1] != 7:
				continue
			if board[x][y] == 'D' and move[1] != 9:
				continue

			if board[x][y] == 'A' and not board[move[0]+1][move[1]] in ['A', '#']:
				continue
			if board[x][y] == 'B' and not board[move[0]+1][move[1]] in ['B', '#']:
				continue
			if board[x][y] == 'C' and not board[move[0]+1][move[1]] in ['C', '#']:
				continue
			if board[x][y] == 'D' and not board[move[0]+1][move[1]] in ['D', '#']:
				continue

		else:
			if move[0] != 1:
				continue

		filtered.append(move)

	return filtered


boards = []
heapq.heappush(boards, (0, board, []))


cache = {}

path_costs = []

while True:
	if not boards:
		break
	cost_sum, board, history = heapq.heappop(boards)

	for move in get_all_moves(board):
		cost, new_board = do_move(copy.deepcopy(board), *move)

		if is_finish(new_board):
			path_costs.append(cost_sum + cost)

		hash = reduce(lambda x, y: x + ''.join(y), new_board, '')
		if hash in cache:
			if cache[hash] <= cost_sum + cost:
				continue
		cache[hash] = cost_sum + cost

		history2 = copy.deepcopy(history)
		history2.append(new_board)
		#history2.append(cost)
		heapq.heappush(boards, (cost_sum + cost, new_board, history2))


print(min(path_costs))