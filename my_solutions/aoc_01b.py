import aocd
import numpy as np
from pathlib  import Path
data_dir = Path.home() / "AOC2021/data/"


file = 'day01b_example.txt'
file = 'day01b.txt'

with open(data_dir / file) as f:
    dta = f.read().splitlines()

dta = list(map(int, [x.split(' ')[0] for x in dta])) #dont need the letters

#better way
pos_diff_sum = sum([(dta[i+3]-dta[i])>0 for i in range(len(dta)-3)])
pos_diff_sum
#
# #dumb way
# summed_dta = [sum(dta[i:i+3]) for i, elmt in enumerate(dta)][:-2]
# diffs = [elmt - summed_dta[i-1] for i, elmt in enumerate(summed_dta)][1:]
# pos_diff_sum = sum([x>0 for x in diffs])
#
#
