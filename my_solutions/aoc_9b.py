session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
from pathlib  import Path
import numpy as np
import pandas as pd
day = 9
example = False
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
        vals = vert_diffs[row, :] > vert_diffs[row - 1, :]
        # vals = vert_diffs[row, :] > 0#vert_diffs[row - 1, :]

    vert_mask[row,:]=vals

horiz_diffs =np.sign(np.diff(height_map, axis=1) )#difference from col to one left col
horiz_mask = np.empty((len(dta), len(dta[0])))
for col in range(horiz_diffs.shape[1]+1):
    if col ==0:
        vals = horiz_diffs[:,0]>0
    elif col ==horiz_diffs.shape[1]:
        vals = horiz_diffs[:,horiz_diffs.shape[1]-1]<0
        # vals = horiz_diffs[:,0]>0
    else:
        vals = horiz_diffs[:, col-1]<horiz_diffs[:, col]
    horiz_mask[:,col]=vals

local_mins = np.multiply(horiz_mask, vert_mask)

basins = horiz_mask+vert_mask

np.multiply(basins>0, height_map)

deep_bois = np.where(basins==2)

#necco, A
class Crawler:
    # row_shift = [-1, -1, -1,  0, 0,  1, 1, 1]
    # col_shift = [-1,  0,  1, -1, 1, -1, 0, 1]
    row_shift = [1, -1, 0,  0]
    col_shift = [0,  0, 1, -1]

    def __init__(self, grid,  deep_boi_spots, col = None, row = None, seent_it = None):
        self.col = 0 if col is None else col
        self.row = 0 if row is None else row
        self.grid = grid
        self.seent_it = np.zeros((self.grid.shape[0], self.grid.shape[1])) if seent_it is None else seent_it
        self.land_tracts = []
        self.this_land = 0
        self.deep_boi_spots = deep_boi_spots

    def is_new(self, row, col, height):
        row_cool = row< self.grid.shape[0] and row>=0
        col_cool = col< self.grid.shape[1] and col>=0
        if row_cool and col_cool:
            monitor_height = self.grid[row,col]
        return row_cool and col_cool and not self.seent_it[row,col] and self.grid[row,col]>height and self.grid[row,col]!=9

    def look_around(self, row, col):
        self.seent_it[row, col]=True
        for direction in range(len(self.row_shift)):
            new_row = row+self.row_shift[direction]
            new_col = col+self.col_shift[direction]
            height = self.grid[row,col]
            if self.is_new(row=new_row, col=new_col,height=height):
                self.this_land+=1
                self.look_around(row = new_row, col = new_col)

    def walkabout(self):
        for self.row, self.col in self.deep_boi_spots:
            self.this_land=1
            self.look_around(row=self.row, col = self.col)
            self.land_tracts.append(self.this_land)
            self.this_land = 0

crawler = Crawler(grid=height_map, deep_boi_spots=list(zip(deep_bois[0], deep_bois[1])))

crawler.walkabout()

np.prod(sorted(crawler.land_tracts)[-3:])