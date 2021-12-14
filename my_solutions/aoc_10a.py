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

match = dict()
openers = '[({<'
closers = '])}>'
for a, b in list(zip(openers, closers)):
    match[a] = b
    match[b] = a

pt_lkup = {')': 3, ']': 57, '}': 1197, '>': 25137}
pts = 0
for line in dta:
    subline = []
    for i, char in enumerate(line):
        if char in openers:
            subline.append(char)
        if char in closers:
            matchme = subline.pop()
            if matchme != match[char]:
                print(f'expecting {match[matchme]} got {char}')
                pts += pt_lkup[char]
                pass

print(pts)
