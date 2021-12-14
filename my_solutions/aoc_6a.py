import aocd
from pathlib import Path
import numpy as np
import pandas as pd
from session.session import get_session

my_session = get_session()
example = False

if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = 'day06a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
        fish_cycle = pd.DataFrame([x.split(': ')[1].split(',') for x in dta])
else:
    dta = aocd.get_data(session=my_session, day=6, year=2021).splitlines()
    fish_cycle = pd.DataFrame([x.split(',') for x in dta])
fishy = fish_cycle.loc[0, :].dropna()


class StupidSexyFlounders():
    def __init__(self, fishy):
        self.fishy = np.array([int(x) for x in fishy])
        self.recycle_idx = None
        self.new_fishies = 0

    def update_age(self):
        self.fishy = np.array([x - 1 for x in self.fishy])

    def birth_update(self):
        if len(self.recycle_idx) > 0:
            self.fishy[self.recycle_idx] = 6
            self.fishy = np.append(self.fishy, np.repeat(8, len(self.recycle_idx)))
        self.recycle_idx = None
        self.new_fishies = 0

    def check_for_births(self):
        self.recycle_idx = list(np.where(self.fishy < 0)[0])
        self.birth_update()

    def fish_cycle(self, iters=1):
        for _ in range(iters):
            self.update_age()
            self.check_for_births()
            # print(self.fishy)

    def how_many(self):
        print(len(self.fishy))


my_sexy_fish = StupidSexyFlounders(fish_cycle.loc[0, :].dropna())
my_sexy_fish.fish_cycle(256)
my_sexy_fish.how_many()
