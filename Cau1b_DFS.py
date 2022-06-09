def graph(nodes, edges):
    graph = {}

    for node in nodes:
        graph[node] = []
        for edge in edges:
            if node == edge[0]:
                if node in graph:
                    graph[node].append(edge[1])
    return graph

def DFS(graph, start, end):
    frontier = [start]
    explored = []

    while frontier:
        state = frontier.pop(len(frontier) - 1)
        explored.append(state)

        if state == end:
            return explored

        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)

    return False

if __name__ == '__main__':
    V = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    E = [('S', 'A'), ('S', 'B'), ('S', 'C'), ('A', 'B'), ('A', 'D'),
        ('B', 'D'), ('B', 'F'), ('B', 'G'), ('C', 'B'), ('C', 'F'),
        ('D', 'E'), ('F', 'E'), ('F', 'H'), ('E', 'G'), ('H', 'G')]

    graph = graph(V, E)

    result = DFS(graph, 'S', 'G')

    if result:
        s = 'explored: '
        for i in result:
            s += i + ' '
            print(s)
    else:
        print('Khong tim thay duong di')