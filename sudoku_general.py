import solver
from copy import deepcopy


def expand(state, x: int, y: int, n: int) -> list:
    current_state = deepcopy(state)
    current_state[y][x] = n
    return current_state


def is_allowed(state, x: int, y: int, n: int) -> bool:
    """
    Checks if it is allowed by sudoku rules to insert specified element in specified position.
    :param state:
    :param x: x coordinate
    :param y: y coordinate
    :param n: number to insert
    """
    state_to_check = expand(state, x, y, n)

    # horizontal fit
    for i in range(9):
        if i == x:
            continue
        if state_to_check[y][i] == n:
            return False

    # vertical fit
    for i in range(9):
        if i == y:
            continue
        if state_to_check[i][x] == n:
            return False

    # smaller squares fit, i - the number of square,
    #                  1 2 3
    #                  4 5 6
    #                  7 8 9
    for i in range(9):
        if ((y // 3) * 3 + i // 3) == y and ((x // 3) * 3 + i % 3) == x:
            continue
        if state[(y // 3) * 3 + i // 3][(x // 3) * 3 + i % 3] == n:
            return False

    return True


def is_goal(state) -> bool:
    for row in state:
        for elem in row:
            if elem == 0:
                return False
    return True


def next_states(state) -> list:
    """
    Finds all possible states after inserting fitting element in the first available position
    :return: List of possible states on the next move
    """
    x_closest = -1
    y_closest = -1
    possibilities = []

    # find the first empty cell
    for i, row in enumerate(state):
        for j, elem in enumerate(row):
            if elem == 0:
                x_closest = j
                y_closest = i
                break
        if x_closest != -1 or y_closest != -1:
            break

    # check all the possible number insertions
    for i in range(9):
        if is_allowed(state, x_closest, y_closest, i + 1):
            possibilities.append(expand(state, x_closest, y_closest, i + 1))

    return possibilities


def is_explored(state: list, to_do) -> bool:
    """
    Right now this only SLOWS the program due to inefficiency of the checking.
    Since the implementation is really naive, it seems to be more efficient to
    not check if the state was already visited at all.

    Checks if the given state was already explored
    :param to_do:
    :param state: State to check
    """
    is_exp = False

    # compare two states element-by-element
    for path in to_do:
        for current_state in path:
            coincide = True
            for i in range(9):
                for j in range(9):
                    if coincide and state[i][j] != current_state[i][j]:
                        coincide = False
            if coincide:
                is_exp = True
                break
        if is_exp:
            break

    return is_exp


def print_board(state: list) -> None:
    """
    Prints board in a well-readable format
    :param state:
    """
    to_print = ""

    for i in range(9):
        for j in range(9):
            to_print += str(state[i][j])
            to_print += ' '
            if j % 3 == 2 and j != 8:
                to_print += '| '
        to_print += '\n'
        if i % 3 == 2 and i != 8:
            to_print += '-----   -----   -----\n'

    print(to_print)


if __name__ == "__main__":
    starting_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]
    ]

    result = solver.depth_first_search(starting_board, is_goal, next_states, is_explored)
    print_board(result[-1])

    result = solver.breadth_first_search(starting_board, is_goal, next_states, is_explored)
    print_board(result[-1])
