from Node import Node
from collections import deque
from Utils import is_in_closed_list


class BDS:
    def __init__(self, root, goal):
        self.root = root
        self.goal = goal
        self.root_closed_list = [[] for _ in range(1000)]
        self.goal_closed_list = [[] for _ in range(1000)]
        self.expanded_nodes = 0

    def search(self):
        root_queue = [self.root]
        goal_queue = [self.goal]
        matched_root = None
        matched_goal = None
        result = []

        while root_queue and goal_queue:
            # searching for match
            for root_child in root_queue:
                for goal_child in goal_queue:
                    if goal_child.compare(root_child):
                        matched_root = root_child
                        matched_goal = goal_child.parent
                        break
                if matched_root: break
            if matched_root: break  # match founded

            for i in range(len(root_queue)):
                current_node = root_queue.pop(0)
                self.root_closed_list[str(current_node.state).__hash__() % 1000].append(
                    str(current_node.state).__hash__())

                for child in current_node.expand():
                    if not is_in_closed_list(self.root_closed_list[str(child.state).__hash__() % 1000],
                                             str(child.state).__hash__()):
                        root_queue.append(child)
                        self.expanded_nodes += 1

            for root_child in root_queue:
                for goal_child in goal_queue:
                    if goal_child.compare(root_child):
                        matched_root = root_child
                        matched_goal = goal_child.parent
                        break
                if matched_root: break
            if matched_root: break  # match founded

            for i in range(len(goal_queue)):
                current_node = goal_queue.pop(0)
                self.goal_closed_list[str(current_node.state).__hash__() % 1000].append(
                    str(current_node.state).__hash__())

                for child in current_node.expand():
                    if not is_in_closed_list(self.goal_closed_list[str(child.state).__hash__() % 1000],
                                             str(child).__hash__()):
                        goal_queue.append(child)
                        self.expanded_nodes += 1
        result.append(matched_root.state)
        for item in matched_root.parents():
            result.append(item.state)
        result.reverse()
        result.append(matched_goal.state)
        for item in matched_goal.parents():
            result.append(item.state)

        return result
