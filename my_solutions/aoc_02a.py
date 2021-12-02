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

direction_map = {'forward': {'direction':'horizontal', 'multiple':1},
'down': {'direction':'depth', 'multiple':1},
'up': {'direction':'depth', 'multiple':-1}
                 }
pos_dict = {'horizontal':0, 'depth':0}

for x in dta:
    instruction, qty = x.split(' ')
    qty=int(qty)
    this_map = direction_map[instruction]
    pos_dict[this_map['direction']]=pos_dict[this_map['direction']]+this_map['multiple']*qty

reduce((lambda x,y: x*y), pos_dict.values())
#