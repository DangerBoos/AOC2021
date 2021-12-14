import aocd
from pathlib import Path
from session.session import get_session  # returns personal session

my_session = get_session()
day = 10
example = False

if example:
    data_dir = Path.home() / "AOC2021/data/"
    file = f'day{day}_example.txt'
    with open(data_dir / file) as f:
        dta = f.read().splitlines()
else:
    dta = aocd.get_data(session=my_session, day=day, year=2021).splitlines()

##########################################################################
match = dict()
openers = '[({<'
closers = '])}>'
for a, b in list(zip(openers, closers)):
    match[a] = b
    match[b] = a

pt_lkup = {')': 1, ']': 2, '}': 3, '>': 4}
pt_list = []
for line in dta:
    subline = []
    pts = 0
    for i, char in enumerate(line):
        if char in openers:
            subline.append(char)
        if char in closers:
            matchme = subline.pop()
            if matchme != match[char]:
                break
    else:
        subline.reverse()
        for i in subline:
            pts = pts * 5 + pt_lkup[match[i]]
        pt_list.append(pts)

pt_list.sort()
print(pt_list[len(pt_list) // 2])
