session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
import pandas as pd
from functools import reduce
from pathlib  import Path
import bitarray
from bitarray.util import ba2int

example = False

if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = 'day03a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=session, day=3, year=2021, block=True).splitlines()

gamma = ''
for col in range(len(dta[0])):
    colsum=0
    for row in range(len(dta)):
        colsum += int(dta[row][col])
    if colsum > len(dta)/2:
        gamma+='1'
    else:
        gamma+='0' #not worryinga bout even split

#this was fucking awful to look up
gamma_ba = bitarray.bitarray(gamma)

epsilon_ba = gamma_ba ^ bitarray.bitarray('1'*len(gamma_ba))
ba2int(gamma_ba)*ba2int(epsilon_ba)

#16 MIN 42 SEC