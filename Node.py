from copy import deepcopy


class Node:
    def __init__(self, state=[], parent=None, depth=0, cost=0, children=[], fn=0):
        self.state = state
        self.parent = parent
        self.children = children
        self.depth = depth
        self.cost = cost
        self.fn = fn

    def expand(self):
        i_zero = None
        j_zero = None

        def swap(x, y):
            new_state = [list(elem) for elem in self.state]
            new_state[x][y], new_state[i_zero][j_zero] = new_state[i_zero][j_zero], new_state[x][y]
            return new_state

        self.children = []

        for i in range(len(self.state)):
            for j in range(len(self.state)):
                if self.state[i][j] == 0:
                    i_zero = i
                    j_zero = j
        # up
        if i_zero != 0:
            self.children.append(Node(swap(i_zero - 1, j_zero), self, self.depth + 1, self.cost + 1, []))
        # down
        if i_zero + 1 != len(self.state):
            self.children.append(Node(swap(i_zero + 1, j_zero), self, self.depth + 1, self.cost + 1, []))
        # left
        if j_zero != 0:
            self.children.append(Node(swap(i_zero, j_zero - 1), self, self.depth + 1, self.cost + 1, []))
        # right
        if j_zero + 1 != len(self.state):
            self.children.append(Node(swap(i_zero, j_zero + 1), self, self.depth + 1, self.cost + 1, []))

        return self.children

    def parents(self):
        current_node = self
        while current_node.parent:
            yield current_node.parent
            current_node = current_node.parent

    def is_goal(self, goal_state):
        if str(self.state).__hash__() == str(goal_state).__hash__():
            return True
        return False

    def set_cost(self, cost):
        self.cost = cost

    def __lt__(self, other):
        return self.fn <= other.fn

    def set_fn(self, fn):
        self.fn = fn

    def compare(self, node):
        if str(self.state).__hash__() == str(node.state).__hash__():
            return True
        else:
            return False
