import aocd
from pathlib import Path
import numpy as np
from session.session import get_session

my_session = get_session()
example = False

if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = 'day04a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=my_session, day=4, year=2021).splitlines()

dta.append('')  # to get split to work
numbers = [int(x) for x in dta[0].split(',')]
boards = [];
board = []
for i, line in enumerate(dta[2:]):
    if line == '':
        boards.append(board)
        board = []
        continue
    board.append(line.strip().replace('  ', ' ').split(' '))

boards = [np.array([np.array(xi) for xi in board]).astype(int) for board in boards]

board_shape = boards[0].shape
matches = [np.empty(board_shape) for _ in range(len(boards))]
winners = [False] * len(boards)

for ball in numbers:
    print(ball)
    for board_idx, board in enumerate(boards):
        if winners[board_idx]:
            pass
        for row, row_val in enumerate(boards[board_idx]):
            match_idx = np.where(row_val == ball)
            matches[board_idx][row, match_idx] = 1
            if np.any(matches[board_idx].sum(axis=1) == board_shape[0]) or np.any(
                    matches[board_idx].sum(axis=0) == board_shape[0]):
                print('winner winner')
                winners[board_idx] = True
                if sum(winners) == len(boards):
                    break
        else:
            continue
        break
    else:
        continue
    break

non_matches = 1 - matches[board_idx]
result = np.sum(np.multiply(non_matches, boards[board_idx])) * ball
print(result)

# np.around(np.multiply(matches[board_idx],boards[board_idx]))
