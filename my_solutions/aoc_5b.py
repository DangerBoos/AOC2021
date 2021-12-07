session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
from pathlib  import Path
import numpy as np
example = False

if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = 'day05a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=session, day=5, year=2021).splitlines()

direction_array = np.array([tuple(map(int, x.split(','))) for line in dta for x in line.split(' -> ')]).reshape(len(dta),4)

x_mask = direction_array[:,0]==direction_array[:,2]
y_mask = direction_array[:,1]==direction_array[:,3]
diag_mask = ((direction_array[:,1]==direction_array[:,0]) & (direction_array[:,2]==direction_array[:,3])) | \
            ((direction_array[:,1]==direction_array[:,2]) & (direction_array[:,0]==direction_array[:,3])) |\
            (abs(direction_array[:,0]-direction_array[:,2]) == abs(direction_array[:,1]-direction_array[:,3]))
x_max= max(np.max(direction_array[:,0]), np.max(direction_array[:, 2]))
y_max= max(np.max(direction_array[:, 1]), np.max(direction_array[:, 3]))

grid = np.zeros((x_max+1,y_max+1))


for mask in x_mask, y_mask,diag_mask:
    print('--------')
    for i in range(direction_array[mask, :].shape[0]):
        row = direction_array[mask,:][i]
        x_start, x_end = row[1], row[3]
        x_step = 1  if row[1] < row[3] else -1
        y_start, y_end = row[0], row[2]
        y_step = 1 if row[0]<row[2] else -1
        y_grid = [y_start] * len(list(np.arange(x_start,x_end+x_step,x_step))) if (y_start == y_end and x_start != x_end) else list(np.arange(y_start,y_end+y_step,y_step))
        x_grid = [x_start] * len(list(np.arange(y_start,y_end+y_step,y_step))) if (x_start == x_end and y_start != y_end) else list(np.arange(x_start,x_end+x_step,x_step))
        for x,y in list(zip(x_grid, y_grid)):
            grid[x, y] += 1

print(np.sum(grid>1))