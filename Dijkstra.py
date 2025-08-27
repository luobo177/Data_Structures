rows,cols = 5,4
graph=[[0 for _ in range(cols)]for _ in range(rows)]

def add_edge(u,v,w):
    graph[u][v] = w

add_edge(0, 1, 2)
add_edge(0, 2, 5)
add_edge(1, 2, 1)
add_edge(1, 3, 3)
add_edge(2, 3, 2)
add_edge(3, 4, 1)