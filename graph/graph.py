class Graph:
    def __init__(self):
        # adjacency list: vertex -> list of (neighbor, weight)
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v, weight=1, directed=True):
        # ensure both vertices exist
        self.add_vertex(u)
        self.add_vertex(v)

        # add edge u -> v
        self.graph[u].append((v, weight))

        # if undirected, add reverse edge
        if not directed:
            self.graph[v].append((u, weight))

    def get_neighbors(self, v):
        return self.graph.get(v, [])

    def __str__(self):
        return str(self.graph)


def dfs(graph, start):
    if start not in graph.graph:
        return []

    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        order.append(node)

        for neighbor, _ in graph.graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return order


from collections import deque

def bfs(graph, start):
    if start not in graph.graph:
        return []

    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor, _ in graph.graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
