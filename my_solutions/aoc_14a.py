import aocd
from session.session import get_session  # returns personal session
from collections import defaultdict

import numpy as np

my_session = get_session()
day = 14
example = False

if example:
    dta = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
else:
    dta = aocd.get_data(session=my_session, day=day, year=2021)

total_steps = 40

template, __rules = dta.split('\n\n')
_rules = [x.split(' -> ') for x in __rules.splitlines()]

# mapping rules
rules = defaultdict(lambda: [])
dr = defaultdict(lambda: '')
for i in range(len(_rules)):
    rules[_rules[i][0]] = [_rules[i][0][0] + _rules[i][1], _rules[i][1] + _rules[i][0][1]]
    dr[_rules[i][0]] = _rules[i][0][0] + _rules[i][1] + _rules[i][0][1]

pair_counts = defaultdict(lambda: 0)
# seed counts
for i in range(len(template) - 1):
    pair_counts[template[i:i + 2]] += 1

for _ in range(total_steps):
    new_pair_counts = defaultdict(lambda: 0)
    for k in list(pair_counts.keys()):
        for new_element in rules[k]:
            new_pair_counts[new_element] += pair_counts[k]
    pair_counts = new_pair_counts.copy()

approx_dbl_letter_counts = defaultdict(lambda: 0)
pair_to_letter_map = dict()

for k in list(rules.keys()):
    pair_to_letter_map[k] = [char for char in k]

for pair in list(pair_counts.keys()):
    for letter in pair_to_letter_map[pair]:
        approx_dbl_letter_counts[letter] += pair_counts[pair]

approx_dbl_letter_counts[template[0]] += 1
approx_dbl_letter_counts[template[-1]] += 1

letter_counts = dict()
for k in approx_dbl_letter_counts:
    letter_counts[k] = approx_dbl_letter_counts[k] / 2

letter_counts_sorted = sorted(letter_counts.items(), key=lambda item: item[1])
print(letter_counts_sorted[-1][1] - letter_counts_sorted[0][1])

# lessons: sort to take max and min!
