import heapq

class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost = 10000
        self.goal_cost = goal_cost
        self.save_cost = None
        self.parent = []
        self.children = []

    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal cost": self.goal_cost
        }))

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        if self.save_cost == 10000:
            return self.goal_cost + self.cost < other.goal_cost + other.cost
        else:
            return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def get_label(self):
        return self.label

    def neighbors(self):
        return self.children + self.parent

class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)

    def add_node(self, node):
        self.nodes.append(node)

    def get_index(self, node):
        for i, n in enumerate(self.nodes):
            if n.get_label() == node.get_label():
                return i
        return -1

    def add_edges(self, tuple_edges):
        for t in tuple_edges:
            start_label = t[0]
            end_label = t[1]
            w = t[2]
            index_start_label = self.get_index(Node(start_label, None))
            index_end_label = self.get_index(Node(end_label, None))
            self.nodes[index_start_label].children.append(
                self.nodes[index_end_label])
            self.nodes[index_end_label].parent.append(
                self.nodes[index_start_label])
            self.edges.append(
                (self.nodes[index_start_label], self.nodes[index_end_label], t[2]))

    def show_nodes(self):
        return [node.get_data() for node in self.nodes]

    def get_edge(self, start_node, end_node):
        try:
            return [edges for edges in self.edges if edges[0] == start_node
                    and edges[1] == end_node][0]
        except:
            return None

def update_cost(tree, current_node, prev_node):
    if tree.get_edge(prev_node, current_node) is not None:
        if current_node.cost > prev_node.cost + tree.get_edge(prev_node, current_node)[2]:
            current_node.cost = prev_node.cost + \
                tree.get_edge(prev_node, current_node)[2]

def a_star(tree, start, end):
    frontier = [start]
    heapq.heapify(frontier)
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        # print(state)
        if state == end:
            return explored
        for child in state.neighbors():
            update_cost(tree, child, state)
            if child.get_label() not in list(set(node.get_label() for node in frontier + explored)):
                heapq.heappush(frontier, child)
    return False

if __name__ == "__main__":
    V = [
        Node("S", 12),  # 0
        Node("A", 9),   # 1
        Node("B", 8),   # 2
        Node("C", 7),   # 3
        Node("D", 6),   # 4
        Node("E", 5),   # 5
        Node("F", 4),   # 6
        Node("G", 10),  # 7
        Node("H", 10),  # 8
        Node("K", 3),   # 9
        Node("M", 9),   # 10
        Node("N", 10),  # 11
        Node("I", 6),   # 12
        Node("J", 0),   # 13
        Node("L", 0),   # 14
        Node("Z", 8)    # 15
    ]
    E = [
        ("S", "A", 5),
        ("B", "B", 6),
        ("S", "C", 5),
        ("A", "D", 6),
        ("A", "E", 7),
        ("B", "F", 3),
        ("B", "G", 4),
        ("C", "H", 6),
        ("C", "K", 4),
        ("D", "M", 5),
        ("D", "N", 8),
        ("E", "I", 8),
        ("F", "J", 4),
        ("F", "L", 4),
        ("K", "Z", 2),
    ]
    tree = Tree()
    tree.add_nodes(V)
    tree.add_edges(E)
    tree.nodes[0].cost = 0
    print('Path from S to J:', end='\n')
    resultJ = a_star(tree, tree.nodes[0], tree.nodes[13])
    if resultJ:
        s = 'explored: '
        for i in resultJ:
            s += i.label + " "
            print(s)
    else:
        print('Path does not exist!')
    print('Path from S to L:', end='\n')
    resultL = a_star(tree, tree.nodes[0], tree.nodes[14])
    if resultL:
        s = 'explored: '
        for i in resultL:
            s += i.label + " "
            print(s)
    else:
        print('Path does not exist!')