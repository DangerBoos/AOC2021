from pathlib import Path

data_dir = Path.home() / "AOC2021/data/"

file = 'day01b_example.txt'
file = 'day01b.txt'

with open(data_dir / file) as f:
    dta = f.read().splitlines()

dta = list(map(int, [x.split(' ')[0] for x in dta]))  # dont need the letters

pos_diff_sum = sum([(dta[i + 3] - dta[i]) > 0 for i in range(len(dta) - 3)])
pos_diff_sum
