import aocd
from pathlib import Path
import bitarray
from bitarray.util import ba2int
from session.session import get_session

my_session = get_session()
example = False

if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = 'day03a_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=my_session, day=3, year=2021, block=True).splitlines()

gamma = ''
for col in range(len(dta[0])):
    colsum = 0
    for row in range(len(dta)):
        colsum += int(dta[row][col])
    if colsum > len(dta) / 2:
        gamma += '1'
    else:
        gamma += '0'  # not worrying about even split

gamma_ba = bitarray.bitarray(gamma)

epsilon_ba = gamma_ba ^ bitarray.bitarray('1' * len(gamma_ba))
ba2int(gamma_ba) * ba2int(epsilon_ba)

# 16 MIN 42 SEC
