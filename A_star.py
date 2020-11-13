import heapq
import sys
import time

from Node import Node
from collections import deque

from UCS import select_min
from Utils import is_in_closed_list
from Heurestics import manhattan_distance


def fn(node, goal_state, hn):
    return hn(node.state, goal_state) + node.depth


class AStar:

    def __init__(self, root, goal):
        self.root = root
        self.goal = goal
        self.closed_list = [[] for _ in range(1000)]
        self.expanded_nodes = 0
        self.visited_nodes = 1

    def search(self, hn):
        self.root.set_fn(fn(self.root, self.goal, hn))
        fringe = [self.root]
        output = []
        current_node = heapq.heappop(fringe)
        while True:
            if is_in_closed_list(self.closed_list[str(current_node.state).__hash__() % 1000],
                                 str(current_node.state).__hash__()):
                current_node = heapq.heappop(fringe)
                continue
            self.visited_nodes += 1
            if current_node.is_goal(self.goal):
                break
            else:
                for child in current_node.expand():
                    child.set_fn(fn(child, self.goal, hn))
                    heapq.heappush(fringe, child)
                    self.expanded_nodes += 1

            self.closed_list[str(current_node.state).__hash__() % 1000].append(str(current_node.state).__hash__())
            current_node = heapq.heappop(fringe)
        print("found in depth {}".format(current_node.depth))
        output.append(current_node.state)
        for parent in current_node.parents():
            output.append(parent.state)

        output.reverse()
        return output
