session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
from pathlib  import Path
import numpy as np
import pandas as pd
day = 9
example = True
if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = f'day0{day}a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=session, day=day, year=2021).splitlines()


height_map = np.array([int(char) for line in  dta for char in line]).reshape((len(dta), len(dta[0])))
vert_diffs =np.sign(np.diff(height_map, axis=0) )#difference from row to row ABOVE
vert_mask =  np.empty((len(dta), len(dta[0])))
for row in range(vert_diffs.shape[0]+1):
    if row ==0:
        vals = vert_diffs[row,:]>0
    elif row==vert_diffs.shape[0]:
        vals=vert_diffs[vert_diffs.shape[0] - 1,:] < 0
    else:
        vals = vert_diffs[row,:]>vert_diffs[row-1,:]
    vert_mask[row,:]=vals

horiz_diffs =np.sign(np.diff(height_map, axis=1) )#difference from col to one left col
horiz_mask = np.empty((len(dta), len(dta[0])))
for col in range(horiz_diffs.shape[1]+1):
    if col ==0:
        vals = horiz_diffs[:,0]>0
    elif col ==horiz_diffs.shape[1]:
        vals = horiz_diffs[:,horiz_diffs.shape[1]-1]<0
    else:
        vals = horiz_diffs[:, col-1]<horiz_diffs[:, col]
    horiz_mask[:,col]=vals

local_mins = np.multiply(horiz_mask, vert_mask)

np.sum(np.multiply(height_map+1,local_mins))