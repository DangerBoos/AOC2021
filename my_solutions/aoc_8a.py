session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
from pathlib  import Path
import numpy as np
import pandas as pd
example = False
if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = 'day08a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=session, day=8, year=2021).splitlines()

dta = pd.DataFrame([x.split(' | ') for x in dta], columns = ['patterns', 'output'])
pattern_cols = ['p_'+str(x) for x in range(10)]; output_cols = ['out_'+str(x) for x in range(4)]
dta[pattern_cols] =dta['patterns'].str.split(' ', expand=True)
dta[output_cols] =dta['output'].str.split(' ', expand=True)
dta.drop(columns = ['patterns', 'output'], inplace=True)
def sort_em(x):
    return ''.join(sorted(x))

dta = dta.applymap(sort_em)

# set(dta.loc[0,pattern_cols])
# set(dta.loc[0,output_cols])
easy_counter=0
for i in range(dta.shape[0]):
    for colname in output_cols:
        elmt = dta.loc[i, colname]
        if len(elmt)==2:
            value=1
        elif len(elmt)==4:
            value=4
        elif len(elmt)==3:
            value=7
        elif len(elmt)==7:
            value=8
            print(elmt)
        else:
            value = elmt
        if value != elmt:
            easy_counter+=1
easy_counter