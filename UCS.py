import sys
import time

from UCS_Node import UcsNode
from collections import deque
from Utils import is_in_closed_list


def select_min(queue):
    min_cost = sys.maxsize
    min_index = None
    for item in queue:
        if item.fn < min_cost:
            min_cost = item.fn
            min_index = queue.index(item)

    return min_index


def select_min_cost(queue):
    min_cost = sys.maxsize
    min_index = None
    for item in queue:
        if item.cost < min_cost:
            min_cost = item.cost
            min_index = queue.index(item)

    return min_index


class UCS:
    def __init__(self, root, goal):
        self.root = root
        self.goal = goal
        self.closed_list = [[] for _ in range(1000)]
        self.visited_nodes = 0
        self.expanded_nodes = 0

    def search(self):
        queue = [self.root]
        output = []

        while queue:
            current_node = queue[select_min_cost(queue)]
            if is_in_closed_list(self.closed_list[str(current_node.state).__hash__() % 1000],
                                 str(current_node.state).__hash__()):
                queue.pop(queue.index(current_node))
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
                queue.pop(queue.index(current_node))


        return output
