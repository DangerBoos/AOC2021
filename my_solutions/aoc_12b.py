session = '53616c7465645f5f909d03044a4bbf4965bb47c0efa80c77dbf8839bf77c0be49f12e2aa2096a0e8b4721d748e199bc9'

import aocd
from collections import defaultdict, deque

from typing import List
from collections import deque
import numpy as np
import pandas as pd
import collections

day = 12
example = False
if example:
   dta = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()
   dta="""dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".splitlines()
else:
    dta = aocd.get_data(session=session, day=day, year=2021).splitlines()

def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList


cave_map = [(x.split('-')[0],x.split('-')[1]) for  x in dta]
adjacency_list = generateAdjacencyLst(cave_map)

# Python program to print all paths from a source to destination.

class Cave:

    def __init__(self, adjacency: dict, src: str,dst: str):
        self.adjacency=adjacency
        self.src = src
        self.dst = dst
        self.paths = []


    def get_paths(self):
        print(len(self.paths))
         # self.paths

    def not_visited(self, node: str, path: List) -> int:
        counter = collections.Counter(path)

        small_caves = [k for k in counter.keys() if k.islower() and k not in ['start', 'end']]
        small_caves_twice = 0
        did_small_twice = False
        visited_too_much = False
        for cave in small_caves:
            if counter[cave]>2:
                visited_too_much=True
            if counter[cave] == 2:
                small_caves_twice += 1
            if small_caves_twice > 1:
                did_small_twice = True

        if did_small_twice or visited_too_much:
            return 0
        else:
            if node in path:
                if node in ['start', 'end']:
                    return 0
        return 1


    # Utility function for finding paths in graph
    # from source to destination
    def findpaths(self) -> None:
        # Create a queue which stores the paths
        q = deque()
        # Path vector to store the current path
        path = [self.src] #maybe
        q.append(path.copy())

        while q:
            path = q.popleft()
            last = path[-1]

            # if destination then print path
            if last == self.dst:
                self.paths.append(path)
            # Traverse to all the nodes connected to current vertex and push new path to queue
            for next_node in self.adjacency[last]:
                if self.not_visited(next_node, path):
                    newpath = path.copy()
                    newpath.append(next_node)
                    q.append(newpath)


# Function for finding the paths
my_cave = Cave(adjacency=adjacency_list, src='start', dst='end')
my_cave.findpaths()
my_cave.get_paths()