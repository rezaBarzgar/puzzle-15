from time import time

from BDS import BDS
from A_star import AStar
from BFS import BFS
from DFS import DFS
from Heurestics import linear_conflict
from IDAstar import IDA
from Node import Node
from Heurestics import *
from UCS import UCS
from UCS_Node import UcsNode
from Utils import standard_printer


def main():
    goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    state = []

    matrix_length = int(input("enter matrix length : "))

    for i in range(matrix_length):
        x = []
        y = input().split(' ')
        for j in range(len(y)):
            x.append(int(y[j]))
        state.append(x)

    # ida_linear_time_start = time()
    # ida_star_linear = IDA(root=Node(state), goal=goal_state)
    # output = ida_star_linear.search(linear_conflict)
    # print("IDA with linear conflict expanded nodes : {}".format(ida_star_linear.expanded_nodes))
    # print("A star with linear conflict visited nodes : {}".format(ida_star_linear.visited_nodes))
    # print("A star with linear conflict execute time : {}\n".format(time() - ida_linear_time_start))

    # ida_manhattan_time_start = time()
    # ida_star_manhattan = IDA(root=Node(state), goal=goal_state)
    # output = ida_star_manhattan.search(manhattan_distance)
    # print("IDA with linear conflict expanded nodes : {}".format(ida_star_manhattan.expanded_nodes))
    # print("A star with linear conflict visited nodes : {}".format(ida_star_manhattan.visited_nodes))
    # print("A star with linear conflict execute time : {}\n".format(time() - ida_manhattan_time_start))

    # a_star_linear = AStar(root=Node(state=state), goal=goal_state)
    # a_star_linear_time_start = time()
    # output = a_star_linear.search(linear_conflict)
    # print("A star with linear conflict expanded nodes : {}".format(a_star_linear.expanded_nodes))
    # print("A star with linear conflict visited nodes : {}".format(a_star_linear.visited_nodes))
    # print("A star with linear conflict execute time : {}\n".format(time() - a_star_linear_time_start))

    # a_star_manhattan = AStar(root=Node(state=state), goal=goal_state)
    # a_star_manhattan_time_start = time()
    # output = a_star_manhattan.search(manhattan_distance)
    # print("A star with manhattan expanded nodes : {}".format(a_star_manhattan.expanded_nodes))
    # print("A star with manhattan visited nodes : {}".format(a_star_manhattan.visited_nodes))
    # print("A star with manhattan execute time : {}\n".format(time() - a_star_manhattan_time_start))

    # bidirectional = BDS(root=Node(state), goal=Node(goal_state))
    # bds_time = time()
    # output = bidirectional.search()
    # print("BDS expand nodes : {} \n".format(bidirectional.expanded_nodes))
    # print("BDS execute time : {}\n".format(time() - bds_time))

    # bfs = BFS(root=Node(state), goal=goal_state)
    # bfs_time = time()
    # output = bfs.search()
    # print("bfs expanded nodes : {}".format(bfs.expanded_nodes))
    # print("bfs visited nodes: {}".format(bfs.visited_nodes))
    # print("bfs execute time: {}\n".format(time() - bfs_time))

    dfs = DFS(root=Node(state), goal=goal_state)
    dfs_time = time()
    output = dfs.search()
    print("dfs expanded nodes : {}".format(dfs.expanded_nodes))
    print("dfs visited nodes: {}".format(dfs.visited_nodes))
    print("dfs execute time: {}\n".format(time() - dfs_time))

    # ucs = UCS(UcsNode(state=state, cost_up=5, cost_down=1, cost_left=1, cost_right=2), goal=goal_state)
    # ucs_time = time()
    # output = ucs.search()
    # print("ucs expanded nodes : {}".format(ucs.expanded_nodes))
    # print("ucs visited nodes: {}".format(ucs.visited_nodes))
    # print("ucs execute time: {}\n".format(time() - ucs_time))

    final_file = open('final.txt', 'w')
    final_file.write(f'{len(state)}\n')

    for out in output:
        for key in out:
            print(key)
        print()
        final_file.write(standard_printer(out))
        final_file.write('\n')


if __name__ == '__main__':
    main()

# [[1, 3, 8, 7], [6, 2, 0, 4], [5, 9, 10, 12], [13, 14, 11, 15]] depth 13
# [[1, 2, 3, 8], [7, 0, 4, 12], [5, 6, 10, 11], [9, 13, 14, 15]] depth 20
# [[9, 4, 6, 8], [13, 15, 3, 11], [5, 14, 1, 2], [10, 7, 12, 0]] depth 40
# [[10, 1, 7, 2], [5, 9, 12, 4], [15, 0, 8, 6], [14, 13, 11, 3]] depth 41
# [[10, 8, 15, 11], [7, 0, 2, 3], [6, 14, 1, 4], [13, 5, 9, 12]] depth 44
# [[9, 2, 7, 14], [11, 8, 10, 13], [1, 6, 0, 3], [15, 5, 12, 4]] depth 50
