import aocd
from pathlib import Path
import numpy as np
import pandas as pd
from collections import defaultdict
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
    dta = aocd.get_data(session=get_session(), day=6, year=2021).splitlines()
    fish_cycle = pd.DataFrame([x.split(',') for x in dta])
fishy = fish_cycle.loc[0, :].dropna()
fish_dict = defaultdict(lambda: 0)
for i in fishy:
    fish_dict[int(i)] += 1


class SexyFish():
    def __init__(self, fishy):
        self.fishy = fishy.copy()
        self.recycle_idx = None
        self.new_fishies = 0

    def update_age(self):
        for k in list(range(-1, 8, 1)):
            self.fishy[k] = self.fishy[k + 1]
            self.fishy[k + 1] = 0

    def birth_update(self):
        if self.fishy[-1] > 0:
            self.fishy[6] += self.fishy[-1]
            self.fishy[8] = self.fishy[-1]
            self.fishy[-1] = 0
        self.fishy[-1] = 0

    def check_for_births(self):
        self.birth_update()

    def fish_cycle(self, iters=1):
        for _ in range(iters):
            self.update_age()
            self.check_for_births()
            # self.pretty_print()

    def pretty_print(self):
        out = []
        for k, v in self.fishy.items():
            out.append([k] * v)
        print(out)

    def how_many(self):
        print(np.sum([v for k, v in self.fishy.items()]))


my_sexy_fish = SexyFish(fish_dict.copy())
my_sexy_fish.fish_cycle(256)
my_sexy_fish.how_many()
