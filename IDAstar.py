import heapq
import sys

from A_star import fn
from Utils import is_in_closed_list


class IDA:
    def __init__(self, root, goal):
        self.root = root
        self.goal = goal
        self.closed_list = [[] for _ in range(1000)]
        self.visited_nodes = 0
        self.expanded_nodes = 0

    def search(self, hn):
        self.root.set_fn(fn(self.root, self.goal, hn))
        min_cutoff = self.root.fn
        current_node = None
        i = 0
        self.visited_nodes = 0
        self.expanded_nodes = 0

        while True:

            cutoff = min_cutoff
            min_cutoff = sys.maxsize
            self.closed_list = [[] for _ in range(1000)]
            fringe = [self.root]

            while fringe:
                current_node = heapq.heappop(fringe)
                if current_node.fn > cutoff:
                    continue
                if is_in_closed_list(self.closed_list[str(current_node.state).__hash__() % 1000],
                                     str(current_node.state).__hash__()):
                    continue
                self.visited_nodes += 1
                if current_node.is_goal(self.goal):
                    break
                else:
                    for child in current_node.expand():
                        child.set_fn(fn(child, self.goal, hn))
                        self.expanded_nodes += 1
                        if child.fn > cutoff:
                            if child.fn < min_cutoff:
                                min_cutoff = child.fn
                        heapq.heappush(fringe, child)
                    self.closed_list[str(current_node.state).__hash__() % 1000].append(
                        str(current_node.state).__hash__())
            if current_node.is_goal(self.goal):
                break
        print('found in {}'.format(current_node.depth))
        output = [current_node.state]
        for parent in current_node.parents():
            output.append(parent.state)

        output.reverse()
        return output
