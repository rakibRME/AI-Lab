
import sys
import time

neighbors = {
    'WA' : ['NT', 'SA'],
    'NT' : ['WA', 'SA', 'Q'],
    'SA' : ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q' :  ['NT', 'SA', 'NSW'],
    'NSW' :  ['Q', 'SA','V'],
    'V' :  ['NSW', 'SA'],
    'T' :  ['']
}
colors = ['Red', 'Green', 'Blue']

states = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

states_where_made_decision_optional = {}

colors_of_states = {}

def check_valid_input():
    for state_key, state_value in neighbors.items():
        if state_key not in states:
            print("State dictionary and list are not matching")
            return False
        for neighbor in state_value:
            if neighbor not in states:
                print("State dictionary_neighbour and state_list are not matching")
                print(neighbor, " is not in the states list, ", state_key," , ",state_value)
                return False
    connection_dict = {}
    for state_key, state_value in neighbors.items():
        for neighbor in state_value:
            connection = ''.join(sorted([state_key, neighbor]))
            if connection in connection_dict.keys():
                connection_dict[connection] = connection_dict[connection] + 1
            else:
                connection_dict[connection] = 1
    for key, value in connection_dict.items():
        if value != 2:
            print("Connection is not valid: ", key)
            return False  
    return True

def if_the_color_is_suitable(state, color):
    for neighbor in neighbors.get(state):
        if colors_of_states.get(neighbor) == color:
            return False
    return True
def return_the_valid_color(state, start_color_index):
    return_color = None
    index = 0

    if index >= len(colors):
        return_color = None
    else:
        for color in colors[start_color_index:]:
            if if_the_color_is_suitable(state, color):
                return_color = color
                break

            index += 1
            if index >= len(colors):
                return_color = None
                break
        
    if return_color == None:
        print("Go to Backtracking", state, start_color_index)
        last_state, last_state_value = states_where_made_decision_optional.popitem()
        return_color = ['backtrack', last_state, last_state_value]
    elif (index != len(colors) - 1):
        states_where_made_decision_optional[state] = return_color
        print("added to the states_where_made_decision_optional: ", state, return_color)
    return return_color

if not check_valid_input():
    print("Please fix the state list and dictionary first")

start_state_index = 0
start_color_index = 0
while start_state_index < len(states):
    state = states[start_state_index]
    output = return_the_valid_color(state,start_color_index)
    print("State: ", state, " Output: ", output)
    if output[0] == 'backtrack':
        start_state_index = states.index(output[1])
        start_color_index = colors.index(output[2])+1
        print("Start State Index: ", start_state_index, " Start Color Index: ", start_color_index)
    else:
        start_color_index = 0
        colors_of_states[state] = output
        start_state_index += 1
print ("where decision made optionally: ",states_where_made_decision_optional)  
print ("final state of the node: ", colors_of_states)


    
