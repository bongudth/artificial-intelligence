from treelib import Tree, Node


def BFS(initalState: Node, goal):
    frontier = [initalState]
    explored = []

    while frontier:
        state = frontier.pop(0)
        explored.append(state)

        if goal == state.tag:
            return explored

        for neighbor in tree.children(state.identifier):
            if neighbor not in (explored and frontier):
                frontier.append(neighbor)

    return False


if __name__ == '__main__':
    tree = Tree()
    tree.create_node('A', 'A')  # root
    tree.create_node('B', 'B', 'A')
    tree.create_node('C', 'C', 'A')
    tree.create_node('D', 'D', 'B')
    tree.create_node('E', 'E', 'B')
    tree.create_node('F', 'F', 'C')
    tree.create_node('G', 'G', 'C')
    tree.create_node('H', 'H', 'D')
    tree.create_node('I', 'I', 'D')
    tree.create_node('J', 'J', 'E')
    tree.create_node('K', 'K', 'E')
    tree.create_node('L', 'L', 'F')
    tree.create_node('M', 'M', 'F')
    tree.create_node('N', 'N', 'G')
    tree.create_node('O', 'O', 'G')

    result = BFS(tree.get_node('A'), 'O')

    if result:
        s = 'explored: '
        for i in result:
            s += i.tag + ' '
            print(s)
    else:
        print('No solution!')
