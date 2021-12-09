session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
from pathlib  import Path
import numpy as np
import pandas as pd
example = False
if example:
    dta=['16,1,2,0,4,2,7,1,2,14']
else:
    dta = aocd.get_data(session=session, day=7, year=2021).splitlines()

dta = np.array([int(x) for x in dta[0].split(',')])
best_point = np.median(dta)
print(np.sum(abs(dta-best_point)))
