#relied on this to guide me to solution: https://www.geeksforgeeks.org/find-paths-given-source-destination/
session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
from collections import defaultdict, deque

from typing import List
from collections import deque
import numpy as np
import pandas as pd
day = 13
example = False
if example:
   dta = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
else:
    dta = aocd.get_data(session=session, day=day, year=2021)

def get_y_trans(y_line):
    translate = np.matrix([[1,0,-1*y_line],[0,1,0],[0,0,1]])
    flip =  np.matrix([[-1,0,0],[0,1,0],[0,0,1]])
    untranslate = np.matrix([[1,0,y_line],[0,1,0],[0,0,1]])
    return untranslate*flip*translate

def get_x_trans(x_line):
    translate = np.matrix([[1, 0, 0], [0, 1, -1 * x_line], [0, 0, 1]])
    flip = np.matrix([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
    untranslate = np.matrix([[1, 0, 0], [0, 1, x_line], [0, 0, 1]])
    return untranslate*flip*translate

dots_,instructions =dta.split('\n\n')
dots = np.array([(int(x.split(',')[1]), int(x.split(',')[0])) for x in dots_.splitlines()])
instructions = [(x.split('=')[0][-1],int(x.split('=')[1]))for x in instructions.splitlines()]

paper = np.zeros(dots.max(axis=0) + 1)
for i in dots:
    paper[tuple(i)]=1

for iter, instruction in enumerate(instructions):
    line_type = instruction[0]
    line_shift = instruction[1]
    if line_type=='y':
        mask = dots[:, 0] > line_shift
        dots_flippable = dots[mask, :]
        trans =  get_y_trans(y_line=line_shift)
    else:
        mask=dots[:, 1] > line_shift
        dots_flippable = dots[mask,:]
        trans = get_x_trans(x_line=line_shift)

    for i in dots_flippable:
        new_pos = tuple(np.array(trans * np.append(i, 1).reshape(3, 1))[0:2])
        paper[new_pos] = 1
    if line_type == 'y':
        paper = paper[:line_shift,:]
    if line_type == 'x':
        paper = paper[:, :line_shift]

    dots = np.transpose(paper.nonzero())



    print(np.sum(paper))
########################################
for i in paper:
    print(''.join([str(int(x)).replace('1','#').replace('0','_') for x in i]))