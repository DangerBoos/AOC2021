import aocd
import numpy as np
from pathlib  import Path
data_dir = Path.home() / "AOC2021/data/"
file = 'day01a.txt'
# file = 'day01_example.txt'

with open(data_dir / file) as f:
    dta = f.read().splitlines()
dta = list(map(int, dta))
# dta = np.array(dta)

diffs = [elmt - dta[i-1] for i, elmt in enumerate(dta)][1:]
pos_diff_sum = sum([x>0 for x in diffs])
pos_diff_sum
# aocd.get_data(day=1, year=2021)
