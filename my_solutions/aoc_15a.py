import aocd
from session.session import get_session  # returns personal session
import heapq
from math import inf
import numpy as np


my_session = get_session()
day = 15
example = False

if example:
    dta = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
else:
    dta = aocd.get_data(session=my_session, day=day, year=2021)

dta = dta.splitlines()
chitenz = np.array([int(char) for line in dta for char in line]).reshape( len(dta[0]), len(dta))
end = (chitenz.shape[0]-1,chitenz.shape[1]-1)
class Chiten():
    row_shift = [1, -1, 0, 0]
    col_shift = [0, 0, 1, -1]

    def __init__(self, start, target, graph):
        self.graph = graph
        self.visited = set()
        self.d = {start: 0}
        self.parent = {start: None}
        self.pq = [(0, start)]
        self.target = target

    def get_adj(self, u):
        row = u[0]
        col = u[1]
        adj_list = []
        for direction in range(len(self.row_shift)):
            new_row = row + self.row_shift[direction]
            new_col = col + self.col_shift[direction]
            if self.is_cool(new_row, new_col):
                adj_list.append(tuple([tuple([new_row,new_col]),self.graph[new_row,new_col]]))
        return adj_list

    def is_cool(self, row, col):
        row_cool = self.graph.shape[0] > row >= 0
        col_cool = self.graph.shape[1] > col >= 0
        not_visited = (row, col) not in self.visited
        return row_cool and col_cool and not_visited

    def dijkstra(self):
        while self.pq:
            du, u = heapq.heappop(self.pq)
            if u in self.visited: continue
            if u == self.target:
                break
            self.visited.add(u)
            for v, weight in self.get_adj(u):
                if v not in self.d or self.d[v] > du + weight:
                    self.d[v] = du + weight
                    self.parent[v] = u
                    heapq.heappush(self.pq, (self.d[v], v))

        return self.parent, self.d

my_lil_chiten = Chiten(start=(0,0), target=end, graph=chitenz)

p,d = my_lil_chiten.dijkstra()
print(d[end])
# d[(chitenz.shape[0]-1,chitenz.shape[1]-1)]