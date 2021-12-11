session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
from pathlib  import Path
import numpy as np
import pandas as pd
day = 10
example = False
if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = f'day{day}_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=session, day=day, year=2021).splitlines()


##########################################################################
match = dict()
openers = '[({<'
closers = '])}>'
for a,b in list(zip(openers,closers)):
    match[a]=b
    match[b]=a

pt_lkup = {')':1, ']':2, '}': 3, '>': 4}
pt_list = []
for line in dta:
    subline = []
    pts = 0
    for i, char in enumerate(line):
        if char in openers:
            subline.append(char)
        if char in closers:
            matchme=subline.pop()
            if matchme!=match[char]:
                break
    else:
        subline.reverse()
        for i in subline:
            pts=pts*5+pt_lkup[match[i]]
        pt_list.append(pts)

pt_list.sort()
print(pt_list[len(pt_list)//2])