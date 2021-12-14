import aocd
import numpy as np
from session.session import get_session

my_session = get_session()
example = False

if example:
    dta = ['16,1,2,0,4,2,7,1,2,14']
else:
    dta = aocd.get_data(session=my_session, day=7, year=2021).splitlines()

dta = np.array([int(x) for x in dta[0].split(',')])
best_point = np.median(dta)
print(np.sum(abs(dta - best_point)))
