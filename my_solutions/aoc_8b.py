import aocd
from pathlib import Path
from collections import defaultdict
import pandas as pd
from session.session import get_session

my_session = get_session()
pd.set_option('display.max_columns', 20)
example = False

if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = 'day08a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=my_session, day=8, year=2021).splitlines()

dta = pd.DataFrame([x.split(' | ') for x in dta], columns=['patterns', 'output'])
pattern_cols = ['p_' + str(x) for x in range(10)];
output_cols = ['out_' + str(x) for x in range(4)]
dta[pattern_cols] = dta['patterns'].str.split(' ', expand=True)
dta[output_cols] = dta['output'].str.split(' ', expand=True)
dta.drop(columns=['patterns', 'output'], inplace=True)


def sort_em(x):
    return ''.join(sorted(x))


def shared(lst):
    return set.intersection(*[set(x) for x in lst])


positions = {0b1000000: None, 0b0100000: None, 0b0010000: None, 0b0001000: None, 0b0000100: None, 0b0000010: None,
             0b0000001: None}

numbers = {0b1110111: 0, 0b0010000 + 0b0000010: 1, 0b1011101: 2, 0b1011011: 3, 0b0111010: 4, 0b1101011: 5, 0b1101111: 6,
           0b1010010: 7, 0b1111111: 8, 0b1111011: 9}

my_sum = 0


def get_decoder(vals):
    positions = {0b1000000: None, 0b0100000: None, 0b0010000: None, 0b0001000: None, 0b0000100: None, 0b0000010: None,
                 0b0000001: None}
    positions[0b0000010] = shared(vals[6]).intersection(shared(vals[2]))  # f
    positions[0b0010000] = shared(vals[2]) - set(positions[0b0000010])  # c
    positions[0b1000000] = shared(vals[3]) - shared(vals[2])  # a
    x2x4 = shared(vals[4]) - shared(vals[2])
    positions[0b0001000] = shared(vals[5]).intersection(x2x4)  # d?
    positions[0b0100000] = shared(vals[6]).intersection(x2x4)  # b
    positions[0b0000001] = shared(vals[5]) - positions[0b0001000] - positions[0b1000000]  # g
    positions[0b0000100] = shared(vals[7]) - set.union(*[v for v in positions.values() if v is not None])
    return {next(iter(v)): k for k, v in positions.items()}


wtf = []
for i in range(dta.shape[0]):
    all_vals = defaultdict(lambda: set())
    for colname in output_cols + pattern_cols:
        elmt = dta.loc[i, colname]
        all_vals[len(elmt)].add(elmt)

    unravel_mystery = get_decoder(vals=all_vals)

    this_num = ''
    for col in output_cols:
        mystery = dta.loc[i, col]
        wtf.append(numbers[sum([unravel_mystery[char] for char in mystery])])
        this_num += str(numbers[sum([unravel_mystery[char] for char in mystery])])
    my_sum += int(this_num)

print(my_sum)
