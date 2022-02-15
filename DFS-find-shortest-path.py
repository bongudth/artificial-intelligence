def DFS_SP(graph, initalState, goal):
    frontier = [[initalState]]
    explored = []

    if initalState == goal:
        print("Same Node")
        return

    while frontier:
        path = frontier.pop(len(frontier) - 1)
        node = path[-1]

        if node not in explored:
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                frontier.append(new_path)

                if neighbor == goal:
                    print("Shortest path:", *new_path)
                    return

            explored.append(node)

    print("No solution!")
    return


if __name__ == "__main__":
    graph = {
        'S': ['A', 'B', 'C'],
        'A': ['D'],
        'B': ['D', 'E', 'G'],
        'C': ['E'],
        'D': ['F'],
        'E': ['F', 'H'],
        'F': ['G'],
        'H': ['G']
    }

    DFS_SP(graph, 'S', 'G')
