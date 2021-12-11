session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
from pathlib  import Path
import numpy as np
import pandas as pd
day = 11
example = True
if example:
   dta = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".splitlines()
else:
    dta = aocd.get_data(session=session, day=day, year=2021).splitlines()

# dta = """11111
# 19991
# 19191
# 19991
# 11111""".splitlines()
#

octo_grid = np.array([int(char) for line in  dta for char in line]).reshape((len(dta), len(dta[0])))

octo_grid[2, 4]

class Shiny:
    row_shift = [-1, -1, -1,  0, 0,  1, 1, 1]
    col_shift = [-1,  0,  1, -1, 1, -1, 0, 1]

    def __init__(self, octo_grid, col = None, row = None, flashed = None, flashes=0):
        self.col = 0 if col is None else col
        self.row = 0 if row is None else row
        self.octo_grid = octo_grid
        self.flashed = np.zeros((self.octo_grid.shape[0], self.octo_grid.shape[1])) if flashed is None else flashed
        self.flashes=0

    def find_flashers(self, df, row_shift=0, col_shift=0):
        eligible_flashers = list(zip(np.where(df > 9)[0], np.where(df > 9)[1]))
        eligible_flashers = [(row_shift+x, col_shift+y) for x,y in eligible_flashers]
        unflashed =  [(x,y) for x,y in eligible_flashers if not self.flashed[x,y]]
        return unflashed

    def update_flashed(self, row_indicator, col_indicator):
        self.flashed[row_indicator, col_indicator]=True

    def keep_flashin(self, row, col, energy):
        energy_check = energy>9
        row_check = row>=0 and row < self.octo_grid.shape[0]
        col_check = col>=0 and col < self.octo_grid.shape[1]
        return energy_check and row_check and col_check

    def get_flash_grid(self, row_indicator, col_indicator):
        row_min = max(row_indicator - 1, 0)
        row_max = min(row_indicator + 2, self.octo_grid.shape[0])
        col_min = max(col_indicator - 1, 0)
        col_max = min(col_indicator + 2, self.octo_grid.shape[1])
        return row_min,row_max,col_min,col_max
        # self.update_flashed(row_indicator,col_indicator)

    def flasher_reaction(self, row_indicator, col_indicator):
        row_min,row_max,col_min,col_max = self.get_flash_grid(row_indicator=row_indicator, col_indicator=col_indicator)
        self.octo_grid[row_min:row_max, col_min:col_max]+=1 #energize
        self.octo_grid[row_indicator, col_indicator]-=1#de-energize the flasher
        self.update_flashed(row_indicator,col_indicator)
        new_flashers = self.find_flashers(df=octo_grid[row_min:row_max, col_min:col_max], row_shift=row_min, col_shift=col_min)
        for row, col in new_flashers:#tricky, old flashes linger
            if self.flashed[row,col]==0:
                self.flasher_reaction(row_indicator=row, col_indicator=col)

    def step(self):
        # self.viz()
        self.flashed=np.zeros((self.octo_grid.shape[0], self.octo_grid.shape[1]))
        self.octo_grid+=1 #energize
        for self.row, self.col in self.find_flashers(df=self.octo_grid):
            if self.flashed[self.row,self.col]==0:
                self.flasher_reaction(self.row, self.col)
        print(np.sum(self.flashed))
        self.flashes+=np.sum(self.flashed)
        self.octo_grid[self.octo_grid>9]=0

    def cycles(self, cycles):
        for _ in range(cycles):
            self.step()

    def viz(self):
        pd_grid = pd.DataFrame(self.octo_grid)
        pd_grid[pd_grid==0]='*'
        print(pd_grid)


crawler = Shiny(octo_grid=octo_grid)
crawler.cycles(cycles=100)
print(crawler.octo_grid)
print(crawler.flashes)
#fuuuuuuuuauuu