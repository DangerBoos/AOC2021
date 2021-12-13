#https://towardsdatascience.com/a-self-learners-guide-to-shortest-path-algorithms-with-implementations-in-python-a084f60f43dc
#https://towardsdatascience.com/search-algorithm-breadth-first-search-with-python-50571a9bb85e
# adjacency matrix/list captures whether pairs of vertices are adjacent or not
adj = {"A": ["B", "C", "D"],
       "B": ["A", "C"],
       "C": ["A", "B"],
       "D": ["A"]}

# Breadth first search:
#  for each node, scan all adjacent nodes
# A GRAPH
#            A
#       /        \
#      B          C
#    /  \        /  \
#   D    E      F    G
#  / \   /\    / \
# H  I  J  K   L  M
#######################
V={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'}

E = [{'A', 'B'}, {'A', 'C'}, {'B', 'D'}, {'B', 'E'}, {'C', 'F'}, {'C', 'G'}, {'D', 'H'},
     {'D', 'I'}, {'E', 'J'}, {'E', 'K'}, {'F', 'L'}, {'F', 'M'}]

from collections import defaultdict, deque

# Generate adjacency list for undirected graph
# Expand all edge pairs: A is connected to B and B is connected to A
def generateAdjacencyLst(edges):
    adjacencyList = defaultdict(list)
    for u, v in edges:
        adjacencyList[u].append(v)
        adjacencyList[v].append(u)
    return adjacencyList

adjacency_list = generateAdjacencyLst(E)
print(adjacency_list)




def bfs(Adj, s):  # Adj: adjacency list, s: starting vertex
    parent = {k:None for k,v in Adj.items()}  # O(V) (use hash if unlabeled)
    parent[s] = s  # O(1) root
    dist = {k:None for k,v in Adj.items()}
    dist[s] = 0 # captures number of steps away from source
    levels = [[s]]  # O(1) initialize levels
    while levels[-1]:  # O(?) last level contains vertices
        frontier = []  # O(1), make new level
        for u in levels[-1]:  # O(?) loop over last full level
            for v in Adj[u]:  # O(Adj[u]) loop over neighbors
                if parent[v] is None:  # O(1) parent not yet assigned
                    parent[v] = u  # O(1) assign parent from levels[-1]
                    dist[v] = dist[u] + 1
                    frontier.append(v)  # O(1) amortized, add to border
        levels.append(frontier)  # add the new level to levels
    return parent, dist
#find all nodes that are one away from the source, then two, ettc,..



parents, distances = bfs(Adj= adjacency_list, s='A')
def bfs(adj, s):
    parent = {s: None}
    d = {s: 0}

    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        for n in adj[u]:
            if n not in d:
                parent[n] = u
                d[n] = d[u] + 1
                queue.append(n)
        return parent, d


def path(node, parent, destination):
    path = []
    while node != destination:
        path.append(node)
        node = parent[node]
    path.append(node)
    return path

path(node='K', parent=parents, destination='A')