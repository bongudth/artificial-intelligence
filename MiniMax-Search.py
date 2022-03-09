from TreeNode import Tree


def max_value(node):
    if len(node.children) == 0:
        return node
    node.goal_cost = -10000
    for child in node.children:
        temp = min_value(child)
        if temp.goal_cost > node.goal_cost:
            node.goal_cost = temp.goal_cost
    return node


def min_value(node):
    if len(node.children) == 0:
        return node
    node.goal_cost = 10000
    for child in node.children:
        temp = max_value(child)
        if temp.goal_cost < node.goal_cost:
            node.goal_cost = temp.goal_cost
    return node


def minimax_search(state):
    max_value(state)


if __name__ == "__main__":
    A = Tree("A")
    B = Tree("B")
    C = Tree("C")
    D = Tree("D")
    E = Tree("E")
    F = Tree("F")
    G = Tree("G")
    H = Tree("H")
    I = Tree("I")
    J = Tree("J")
    K = Tree("K")
    L = Tree("L")
    M = Tree("M")
    N = Tree("N")
    Z = Tree("Z")
    A.add_child(B)
    A.add_child(C)
    B.add_child(D)
    B.add_child(E)
    C.add_child(F)
    C.add_child(G)
    D.add_child(H)
    D.add_child(I)
    E.add_child(J)
    E.add_child(K)
    F.add_child(M)
    F.add_child(N)
    G.add_child(L)
    G.add_child(Z)
    H.goal_cost = 2
    I.goal_cost = 9
    J.goal_cost = 7
    K.goal_cost = 4
    M.goal_cost = 8
    N.goal_cost = 9
    L.goal_cost = 3
    Z.goal_cost = 5

    minimax_search(A)
    print(A.goal_cost)
