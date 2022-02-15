def DFS(initalState, goal):
    frontier = [initalState]
    explored = []

    while frontier:
        s = 'frontier: '
        for i in frontier:
            s += i + ' '
        print(s)

        state = frontier.pop(len(frontier) - 1)
        explored.append(state)

        if goal == state:
            return explored

        for neighbor in graph[state]:
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)

    return False


if __name__ == '__main__':
    graph = {
    	'A': ['B', 'C'],
    	'B': ['D', 'E'],
    	'C': ['F', 'G'],
    	'D': ['H', 'I'],
    	'E': ['J', 'K'],
    	'F': ['L', 'M'],
    	'G': ['N', 'O'],
    	'H': [],
    	'I': [],
    	'J': [],
    	'K': [],
    	'L': [],
    	'M': [],
    	'N': [],
    	'O': []
    }

    result = DFS('A', 'H')
