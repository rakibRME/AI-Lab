grid_height = 3
grid_width = 4
grid_state = {(1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0,
              (2, 1): 0, (2, 2): 'None', (2, 3): 0, (2, 4): 0,
              (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0
              }
action_policy = {}

def get_reward(a, b):
    if (a, b) == (1, 4):
        return +1.00
    elif (a, b) == (2, 4):
        return -1.00
    else:
        return 0

def is_goal_state(a, b):
    if (a, b) == (1, 4) or (a, b) == (2, 4):
        return True
    else:
        return False

def is_obstacle(a, b):
    if (a, b) == (2, 2):
        return True
    else:
        return False

def find_neighbors(a, b):
    global grid_state, grid_height, grid_width
    neighbors = {}

    if is_obstacle(a, b):
        return

    if b >= 1:
        if not is_goal_state(a, b):
            if b == 1:
                neighbors['left'] = (a, b)

            else:
                if is_obstacle(a, b - 1):
                    neighbors['left'] = (a, b)
                else:
                    neighbors['left'] = (a, b - 1)

    if b <= grid_width:
        if not is_goal_state(a, b):
            if b == grid_width:
                neighbors['right'] = (a, b)
            else:
                if is_obstacle(a, b + 1):
                    neighbors['right'] = (a, b)
                else:
                    neighbors['right'] = (a, b + 1)
        else:
            neighbors['right'] = 'exit'

    if a >= 1:
        if not is_goal_state(a, b):
            if a == 1:
                neighbors['up'] = (a, b)
            else:
                if is_obstacle(a - 1, b):
                    neighbors['up'] = (a, b)
                else:
                    neighbors['up'] = (a - 1, b)

    if a <= grid_height:
        if not is_goal_state(a, b):
            if a == grid_height:
                neighbors['down'] = (a, b)
            else:
                if is_obstacle(a + 1, b):
                    neighbors['down'] = (a, b)
                else:
                    neighbors['down'] = (a + 1, b)

    return neighbors

def display_grid():
    global grid_state, grid_height, grid_width
    for i in range(1, grid_height + 1):
        for j in range(1, grid_width + 1):
            value = grid_state[(i, j)]
            if value != 'None':
                grid_state[(i, j)] = format(value, '.2f')
                print(grid_state[(i, j)], end='   ')
            else:
                grid_state[(i, j)] = value
                print(grid_state[(i, j)], end='   ')

        print('\n')

def display_policy():
    print('\n\n')
    global grid_state, grid_height, grid_width, action_policy
    for i in range(1, grid_height + 1):
        for j in range(1, grid_width + 1):
            print(action_policy[(i, j)], end='   ')
        print('\n')

def iterate_values():
    global grid_state, grid_height, grid_width, action_policy
    discount_factor = 0.9
    previous_grid = {}
    possible_actions = ['up', 'down', 'right', 'left']
    while True:
        previous_grid = grid_state.copy()
        for i in range(1, grid_height + 1):
            for j in range(1, grid_width + 1):
                current_value = grid_state[(i, j)]
                current_reward = get_reward(i, j)

                if is_obstacle(i, j):
                    grid_state[(i, j)] = previous_grid[(i, j)]
                    action_policy[(i, j)] = "|-_-_-|"

                if is_goal_state(i, j):
                    maximum_value = current_reward
                    grid_state[(i, j)] = maximum_value
                    action_policy[(i, j)] = 'Terminal'

                else:
                    neighbor_states = find_neighbors(i, j)
                    if neighbor_states is None:
                        continue
                    for move in possible_actions:
                        if move == 'left':
                            target_state = neighbor_states['left']
                            alternative_state1 = neighbor_states['up']
                            alternative_state2 = neighbor_states['down']
                            maximum_value = (0.8 * discount_factor * previous_grid[target_state]) + (0.1 * discount_factor * previous_grid[alternative_state1]) + (
                                    0.1 * discount_factor * previous_grid[alternative_state2])
                            if maximum_value > current_value:
                                grid_state[(i, j)] = maximum_value
                                action_policy[(i, j)] = 'left '

                        if move == 'right':
                            target_state = neighbor_states['right']
                            alternative_state1 = neighbor_states['up']
                            alternative_state2 = neighbor_states['down']
                            maximum_value = (0.8 * discount_factor * previous_grid[target_state]) + (0.1 * discount_factor * previous_grid[alternative_state1]) + (
                                    0.1 * discount_factor * previous_grid[alternative_state2])
                            if maximum_value > current_value:
                                grid_state[(i, j)] = maximum_value
                                action_policy[(i, j)] = 'right'

                        if move == 'up':
                            target_state = neighbor_states['up']
                            alternative_state1 = neighbor_states['left']
                            alternative_state2 = neighbor_states['right']
                            maximum_value = (0.8 * discount_factor * previous_grid[target_state]) + (0.1 * discount_factor * previous_grid[alternative_state1]) + (
                                    0.1 * discount_factor * previous_grid[alternative_state2])
                            if maximum_value > current_value:
                                grid_state[(i, j)] = maximum_value
                                action_policy[(i, j)] = ' up '

                        if move == 'down':
                            target_state = neighbor_states['down']
                            alternative_state1 = neighbor_states['left']
                            alternative_state2 = neighbor_states['right']
                            maximum_value = (0.8 * discount_factor * previous_grid[target_state]) + (0.1 * discount_factor * previous_grid[alternative_state1]) + (
                                    0.1 * discount_factor * previous_grid[alternative_state2])
                            if maximum_value > current_value:
                                grid_state[(i, j)] = maximum_value
                                action_policy[(i, j)] = 'down '

        if previous_grid == grid_state:
            break

iterate_values()
display_grid()
display_policy()
