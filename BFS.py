import time

from Node import Node
from collections import deque
from Utils import is_in_closed_list


class BFS:  # Breadth-first search
    def __init__(self, root, goal):
        self.root = root
        self.goal = goal
        self.closed_list = [[] for _ in range(1000)]
        self.expanded_nodes = 0
        self.visited_nodes = 1

    def search(self):
        queue = [self.root]
        output = []

        while queue:
            current_node = queue.pop(0)
            if is_in_closed_list(self.closed_list[str(current_node.state).__hash__() % 1000],
                                 str(current_node.state).__hash__()):
                continue
            self.visited_nodes += 1
            if current_node.is_goal(goal_state=self.goal):
                output.append(current_node.state)
                for parent in current_node.parents():
                    output.append(parent.state)
                output.reverse()
                break
            else:
                for child in current_node.expand():
                    queue.append(child)
                    self.expanded_nodes += 1
                self.closed_list[str(current_node.state).__hash__() % 1000].append(str(current_node.state).__hash__())
        return output
