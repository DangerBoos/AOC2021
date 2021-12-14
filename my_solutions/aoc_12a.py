# relied on this to guide me to solution: https://www.geeksforgeeks.org/find-paths-given-source-destination/
import aocd
from collections import defaultdict, deque
from typing import List
from session.session import get_session  # returns personal session

my_session = get_session()
day = 12
example = False

if example:
    dta = """dc-end
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
    dta = aocd.get_data(session=my_session, day=day, year=2021).splitlines()


def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList


cave_map = [(x.split('-')[0], x.split('-')[1]) for x in dta]
adjacency_list = generateAdjacencyLst(cave_map)


# Python program to print all paths from a source to destination.

class Cave:

    def __init__(self, adjacency: dict, src: str, dst: str):
        self.adjacency = adjacency
        self.src = src
        self.dst = dst
        self.paths = []

    def get_paths(self):
        print(len(self.paths))
        # self.paths

    def not_visited(self, node: str, path: List) -> int:
        if node in path and (node.islower() or node == 'start'):
            return 0
        return 1

    # Utility function for finding paths in graph
    # from source to destination
    def findpaths(self) -> None:
        # Create a queue which stores the paths
        q = deque()
        # Path vector to store the current path
        path = [self.src]  # maybe
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
