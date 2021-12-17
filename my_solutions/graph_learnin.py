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

#############################################################################


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
#############################################################################
def bfs2(adj, s):
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

parents, distances = bfs2(adj= adjacency_list, s='A')

def path(node, parent, destination):
    path = []
    while node != destination:
        path.append(node)
        node = parent[node]
    path.append(node)
    return path

path(node='K', parent=parents, destination='A')



#############################################################################
#Not a shortest path algo...
# maybe look into it later?
def dfs(adj, v, parent, order):
    if not parent:
        parent[v] = None
    # checking neighbours of v
    for n in adj[v]:
        if n not in parent:
            parent[n] = v
            dfs(adj, n, parent, order)

    # we're done visiting a node only when we're done visiting
    # all of its descendents first
    order.append(v)




###################
# EDGE RELAXATION #
###################
#real code but not used:
def Relax(u, v, weight, parent, dist):
    if dist[v] > dist[u] + weight(u, v):
        dist[v] = dist[u] + weight(u, v)
        parent[v] = u
# we have some distance to v (perhaps initialized to INF) then we check if the current distance to V is greater than
 # distance to U + weight(u,v).  If so, dist(v) is updated to distance going through u-v edge.  AND we update parent of
 # V to be U (since that's the best way to get there.

 #PSEUDO CODE (find the path to node from all adjacent nodes):
 #1. Select edge (u, v) from the graph.
 #2.  Relax edge (u, v).
 #3. repeat 1 and 2, selecting edges in some order, until no edges can be relaxed (d[v] ≤ d[a] + weight(a, v) for all edges (a, v))
 # Pick all edges leading to this point and find the shortest one.  Now on to how we pick these edges


###################
#   BELLMAN FORD  #
###################
# didn't understand it quickly and it uses negative weights so moving on

###################
#    DJIKSTRA     #
###################
# The reason I came here anyway
#             A
#       /2   3|   7 \
#      B      C      D

#What's the shortest path to C

# Pseudo-code Dijkstra (adj, source):
# visited = {}
# Q = priority_queue()
# Initialize Q with (node, distance) values, distance being 0 for the source and infinity for every other node.
# while Q is not empty:
#     u = extract_min(Q) # deletes u from Q
#     visited = visited ∪ {u}
#     for each vertex v, weight in Adj[u]:
#         if d[v] > d[u] + weight(u, v):
#             d[v] = d[u] + weight(u, v)
#             parent[v] = u
#             Q.decrease_key(v, d[v])