from copy import deepcopy


def depth_first_search(initial_state, goal_func, next_states_func, is_explored_func):
    to_do = [[initial_state]]  # virtual stack
    while to_do:
        current_path = to_do.pop()
        current_state = current_path[-1]
        if goal_func(current_state):
            return current_path
        for state in next_states_func(current_state):
            if not is_explored_func(state, to_do):  # only add unexplored states
                to_append = deepcopy(current_path)
                to_append.append(state)
                to_do.append(to_append)
    raise Exception("No path found")


def breadth_first_search(initial_state, goal_func, next_states_func, is_explored_func):
    to_do = [[initial_state]]  # virtual queue
    while to_do:
        current_path = to_do.pop()
        current_state = current_path[-1]
        if goal_func(current_state):
            return current_path
        for state in next_states_func(current_state):
            is_explored = is_explored_func(state, to_do)
            if not is_explored:  # only add unexplored states
                to_append = deepcopy(current_path)
                to_append.append(state)
                to_do.insert(0, to_append)
    raise Exception("No path found")


if __name__ == "__main__":
    print('hi')
