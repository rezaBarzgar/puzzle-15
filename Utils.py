def is_in_closed_list(closed, node):
    for item in closed:
        if item == node:
            return True

    return False


def standard_printer(state):
    x = ''
    for i in state:
        for j in i:
            x += str(j)
            x += ','
    x = x[0:len(x) - 1]
    return x
