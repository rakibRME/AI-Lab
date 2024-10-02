class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.children = []
        self.value = value
        self.alpha = float('-inf')
        self.beta = float('inf')

def build_tree(parents, values):
    node_dict = {}
    for parent, children in parents.items():
        if parent not in node_dict:
            node_dict[parent] = Node(parent)

        for child in children:
            if child not in node_dict:
                node_dict[child] = Node(child)

            if child in values:
                node_dict[child].value = values[child]

            node_dict[parent].children.append(node_dict[child])

    return node_dict['A']

def alpha_beta_pruning(node, maximizing_player, alpha, beta, visited, pruned, path):
    visited.append(node.name)
    path.append(node.name)

    if not node.children:
        return node.value

    if maximizing_player:
        value = float('-inf')
        for i, child in enumerate(node.children):
            child_value = alpha_beta_pruning(child, False, alpha, beta, visited, pruned, path)
            value = max(value, child_value)
            alpha = max(alpha, value)

            if alpha >= beta:
                if i + 1 < len(node.children):
                    next_child = node.children[i + 1]
                    pruned.extend(get_all_child_names(next_child))
                break
        return value
    else:
        value = float('inf')
        for i, child in enumerate(node.children):
            child_value = alpha_beta_pruning(child, True, alpha, beta, visited, pruned, path)
            value = min(value, child_value)
            beta = min(beta, value)

            if alpha >= beta:
                if i + 1 < len(node.children):
                    next_child = node.children[i + 1]
                    pruned.extend(get_all_child_names(next_child))
                break
        return value

def get_optimal_path(node, target_node):
    if node.name == target_node:
        return [node.name]

    for child in node.children:
        path = get_optimal_path(child, target_node)
        if path:
            return [node.name] + path

    return []

def get_all_child_names(node):
    names = [node.name]
    for child in node.children:
        names.extend(get_all_child_names(child))
    return names

def find_node_with_value(node, target_value):
    if node.value == target_value:
        return node.name

    for child in node.children:
        result = find_node_with_value(child, target_value)
        if result:
            return result

    return None

def get_optimal_value_policy_and_path(filename):
    with open(filename, 'r') as file:
        node_info = file.readline().strip().split()
        non_terminal_nodes = int(node_info[0])
        root_node = node_info[1]

        parents = {}
        for _ in range(non_terminal_nodes):
            line = file.readline().strip().split()
            parent = line[0]
            children = line[1:]
            parents[parent] = children

        terminal_nodes = int(file.readline().strip())
        values_line = file.readline().strip().split()
        values = {values_line[i]: int(values_line[i + 1]) for i in range(0, len(values_line), 2)}

    root = build_tree(parents, values)
    visited_nodes = []
    pruned_branches = []
    path = []
    optimal_value = alpha_beta_pruning(root, True, float('-inf'), float('inf'), visited_nodes, pruned_branches, path)
    optimal_node_name = find_node_with_value(root, optimal_value)

    if optimal_node_name:
        optimal_path = get_optimal_path(root, optimal_node_name)
        return optimal_value, optimal_path, visited_nodes, pruned_branches
    else:
        return optimal_value, [], visited_nodes, pruned_branches

filename = 'alpha_beta_pruning.txt'
optimal_value, optimal_path, visited_nodes, pruned_branches = get_optimal_value_policy_and_path(filename)

print(f"Optimal Value: {optimal_value}")
print(f"Optimal Path: {optimal_path}")
#print(f"Visited Nodes: {visited_nodes}")
print(f"Pruned Branches: {pruned_branches}")
