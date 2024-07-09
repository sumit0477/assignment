
### 2. `main.py`

```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def input_graph():
    n = int(input("Enter the number of nodes: "))
    graph = [[] for _ in range(n)]
    for i in range(n):
        edges = input(f"Enter edges and weights from node {i} in the format 'j,w; k,w; ...': ")
        if edges:
            edges = edges.split(';')
            for edge in edges:
                if edge.strip():
                    j, w = map(int, edge.strip().split(','))
                    graph[i].append((j, w))
    return graph

def longest_path(graph: list) -> int:
  # Your implementation goes here
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
  # Your implementation goes here
    n = len(graph)
    visited = [False] * n
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]

def calculate_longest_path(graph, topo_order):
  # Your implementation goes here
    n = len(graph)
    dist = [-float('inf')] * n  
    
    for start in topo_order:
        if dist[start] == -float('inf'):
            dist[start] = 0
        for node in topo_order:
            if dist[node] != -float('inf'):
                for neighbor, weight in graph[node]:
                    if dist[neighbor] < dist[node] + weight:
                        dist[neighbor] = dist[node] + weight
    
    return max(dist)

graph = input_graph()
print("Longest path length:", longest_path(graph))
