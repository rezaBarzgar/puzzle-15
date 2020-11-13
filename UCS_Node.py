from copy import deepcopy

from Node import Node


class UcsNode(Node):

    def __init__(self, state=[], parent=None, depth=0, cost=0, children=[], cost_up=1, cost_down=1, cost_right=1,
                 cost_left=1):
        self.state = state
        self.parent = parent
        self.children = children
        self.depth = depth
        self.cost = cost
        self.cost_up = cost_up
        self.cost_down = cost_down
        self.cost_right = cost_right
        self.cost_left = cost_left

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
            self.children.append(Node(swap(i_zero - 1, j_zero), self, self.depth + 1, self.cost + self.cost_up, []))
        # down
        if i_zero + 1 != len(self.state):
            self.children.append(Node(swap(i_zero + 1, j_zero), self, self.depth + 1, self.cost + self.cost_down, []))
        # left
        if j_zero != 0:
            self.children.append(Node(swap(i_zero, j_zero - 1), self, self.depth + 1, self.cost + self.cost_left, []))
        # right
        if j_zero + 1 != len(self.state):
            self.children.append(Node(swap(i_zero, j_zero + 1), self, self.depth + 1, self.cost + self.cost_right, []))

        return self.children
