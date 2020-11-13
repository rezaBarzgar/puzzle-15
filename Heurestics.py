def manhattan_distance(state, goal):
    tiles_places = []
    for i in range(len(goal)):
        for j in range(len(goal)):
            tiles_places.append((goal[i][j], (i, j)))
    cost = 0
    for i in range(len(state)):
        for j in range(len(state)):
            tile_i, tile_j = tiles_places[state[i][j] - 1][1]
            if i != tile_i or j != tile_j:
                cost += abs(tile_i - i) + abs(tile_j - j)

    return cost


def linear_conflict(state, goal):
    cost = 0
    goal_transpose = [*zip(*goal)]
    goal_transpose = [list(elem) for elem in goal_transpose]
    state_transpose = [*zip(*state)]
    state_transpose = [list(elem) for elem in state_transpose]
    tiles_places = []
    tiles_places_transport = []
    for i in range(len(goal)):
        for j in range(len(goal)):
            tiles_places.append((goal[i][j], (i, j)))

    for j in range(len(goal_transpose)):
        for i in range(len(goal_transpose)):
            tiles_places_transport.append((goal_transpose[i][j], (i, j)))

            # finding row conflicts
    for i in range(len(state)):
        for j in range(len(state)):
            if i == tiles_places[state[i][j] - 1][1][0] and state[i][j] != 0:
                for k in range(j + 1, len(state)):
                    if i == tiles_places[state[i][k] - 1][1][0] and state[i][k] != 0:
                        if state[i][j] > state[i][k]:
                            cost += 1
            # finding col conflicts
    for i in range(len(state_transpose)):
        for j in range(len(state_transpose)):
            if i == tiles_places_transport[state_transpose[i][j] - 1][1][0] and state_transpose[i][j] != 0:
                for k in range(j + 1, len(state_transpose)):
                    if i == tiles_places_transport[state_transpose[i][k] - 1][1][0] and state_transpose[i][k] != 0 and \
                            state_transpose[i][j] > state_transpose[i][k]:
                        cost += 1
    return cost * 2 + manhattan_distance(state, goal)
