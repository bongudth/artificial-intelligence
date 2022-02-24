class Node(object):
    def __init__(self, label: str = None):
        self.label = label
        self.children = []

    def __lt__(self, other):
        return (self.label < other.label)

    def __gt__(self, other):
        return (self.label > other.label)

    def __repr__(self):
        return '{} -> {}'.format(self.label, self.children)

    def add_child(self, node, cost=1):
        edge = Edge(self, node, cost)
        self.children.append(edge)


class Edge(object):
    def __init__(self, source: Node, destination: Node, cost: int = 1):
        self.source = source
        self.destination = destination
        self.cost = cost

    def __repr__(self):
        return '{}: {}'.format(self.cost, self.destination.label)


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
J = Node('J')
K = Node('K')
L = Node('L')
M = Node('M')
N = Node('N')
O = Node('O')

A.add_child(B, 2)
A.add_child(C, 1)
A.add_child(D, 3)

B.add_child(E, 5)
B.add_child(F, 4)

C.add_child(G, 6)
C.add_child(H, 3)

D.add_child(I, 2)
D.add_child(J, 4)

F.add_child(K, 2)
F.add_child(L, 1)
F.add_child(M, 4)

H.add_child(N, 2)
H.add_child(O, 4)

[print(node) for node in [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O]]
print('\n')
