session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
import pandas as pd
from functools import reduce
from pathlib  import Path
import bitarray
from bitarray.util import ba2int
from itertools import compress

example = False

if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = 'day03a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=session, day=3, year=2021, block=True).splitlines()

dta_orig = dta.copy()
dtas = []
for iter in range(2):
    dta = dta_orig.copy()
    for col in range(len(dta[0])):
        colsum=0
        for row in range(len(dta)):
            colsum += int(dta[row][col])
        if colsum >= len(dta)/2:
            gamma='1' if iter==0 else '0'
        else:
            gamma='0' if iter==0 else '1' #not worryinga bout even split in part a

        dta_mask = []
        for row in range(len(dta)):
            you_lil_bit = bitarray.bitarray(dta[row][col])
            dta_mask.append(bool(you_lil_bit == bitarray.bitarray(gamma)))
        dta = list(compress(dta,dta_mask))
        if len(dta)==1:
            break
    dtas.append(dta.copy()[0])


dta_bits = [bitarray.bitarray(x) for x in dtas]
ba2int(dta_bits[0])*ba2int(dta_bits[1])

#34 min 20 sec