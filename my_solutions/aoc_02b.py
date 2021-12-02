session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
import numpy as np
from functools import reduce
from pathlib  import Path

example = False

if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = 'day02a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=session, day=2, year=2021, block=True).splitlines()


class sub:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0

    def report_position(self):
        print(f'horizontal position: {self.horizontal}')
        print(f'depth: {self.depth}')

    def update_horizontal(self, qty):
        self.horizontal+=qty

    def update_depth(self, qty):
        self.depth = self.depth + self.aim*qty

    def go_forward(self, qty):
        self.update_horizontal(qty)
        self.update_depth(qty)

    def go_down(self, qty):
        self.aim = self.aim + qty

    def go_up(self, qty):
        self.aim = self.aim - qty

    def follow_instructions(self, instruction):
        direction, qty = instruction.split(' ')
        qty = int(qty)
        if direction =='forward':
            self.go_forward(qty)
        if direction =='down':
            self.go_down(qty)
        if direction =='up':
            self.go_up(qty)

    def get_product(self):
        return self.depth*self.horizontal



my_sub = sub()
for i in dta:
    my_sub.follow_instructions(i)

my_sub.get_product()