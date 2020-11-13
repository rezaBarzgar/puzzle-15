from Utils import is_in_closed_list


class DFS:  # depth-first search
    def __init__(self, root, goal):
        self.root = root
        self.goal = goal
        self.closed_list = [[] for _ in range(1000)]
        self.visited_nodes = 0
        self.expanded_nodes = 0

    def search(self):
        stack = [self.root]

        output = []
        while stack:
            current_node = stack.pop()

            if is_in_closed_list(self.closed_list[str(current_node.state).__hash__() % 1000],
                                 str(current_node.state).__hash__()):  # recursive ba parent ha
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
                    stack.append(child)
                    self.expanded_nodes += 1
                self.closed_list.append(current_node)
        return output
