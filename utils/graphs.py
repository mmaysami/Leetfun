"""
# -------------------------------------------------------------------------------
# Name:         Tree
# Purpose:      Directed Graph Utilities
#
#
# Author:       Moe Maysami
#
# Created:      Jan 2022
# Licence:      See Git
# -------------------------------------------------------------------------------
"""
from collections import defaultdict, deque

# -------------------------------------------------------------------------------
class Graph:
    """
    Directed Graph Class
        Alphanumerical Vertex Labels
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def set_by_dict(self, dict):
        self.graph = dict

    def add_edge(self, v1, v2):
        """
        Append Edge from vertex 1 to vertex 2

        :param v1:   Source Vertex (Int)
        :param v2:   Target Vertex (Int)
        :return:
        """
        self.graph[v1].append(v2)

    # -------------------------------------------------------------------------------
    def bfs(self, start):
            """
            Print Breath First Search (Level Order)

            :param start:   Starting Vertex
            :return:
            """
            # Init Start Vertex and Report it
            visited = [start]

            que = deque()
            que.append(start)

            while que:
                s = que.popleft()
                print(s, end=',')

                for v in self.graph[s]:
                    if v not in visited:
                        que.append(v)
                        visited.append(v)
                        # print('\ns, v, q', s, v, list(que))

    # -------------------------------------------------------------------------------
    def dfs(self, start, visited=[]):
        """
        Print Depth First Search

        :param start:   Starting Vertex
        :return:
        """

        if visited is None:
            visited = []
        elif start in visited:
            return

        # Init Start Vertex and Report it
        visited.append(start)
        que = deque()
        que.append(start)

        while que:
            s = que.popleft()
            print(s, end=',')

            for v in self.graph[s]:
                if v not in visited:
                    self.dfs(v, visited)
                    # print('\ns, v, q', s, v, list(que))


# ================================================================================
#   Tests
# ================================================================================
g1 = Graph()
g1.set_by_dict({
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
})

g2 = Graph()
g2.set_by_dict({
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
})

cases = [g1]
sb = 2
sd = 1

for d in cases:
    print('\nData: ', d.graph)
    print('\nBFS Start: ', sb)
    d.bfs(sb)
    print('\nDFS Start: ', sd)
    d.dfs(sd)
