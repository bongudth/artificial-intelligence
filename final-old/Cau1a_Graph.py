def graph(nodes, edges):
    graph = {}

    for node in nodes:
        graph[node] = []
        for edge in edges:
            if node == edge[0]:
                if node in graph:
                    graph[node].append(edge[1])
    return graph

if __name__ == '__main__':
    V = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    E = [('S', 'A'), ('S', 'B'), ('S', 'C'), ('A', 'B'), ('A', 'D'),
        ('B', 'D'), ('B', 'F'), ('B', 'G'), ('C', 'B'), ('C', 'F'),
        ('D', 'E'), ('F', 'E'), ('F', 'H'), ('E', 'G'), ('H', 'G')]

    graph = graph(V, E)