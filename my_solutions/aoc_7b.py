import aocd
import numpy as np
from session.session import get_session

my_session = get_session()
example = False

if example:
    dta = ['16,1,2,0,4,2,7,1,2,14']
else:
    dta = aocd.get_data(session=get_session(), day=7, year=2021).splitlines()

dta = np.array([int(x) for x in dta[0].split(',')])
min_penalty = 1e12
penalties = []

# brute force because I'm short on time today
for best_candidate in range(1000):
    penalty = np.sum(abs(dta - best_candidate) * (abs(dta - best_candidate) + 1) / 2)
    if penalty < min_penalty:
        min_penalty = penalty
        best_point = best_candidate
    penalties.append(penalty)
    if penalty > min_penalty:
        break

min_penalty
