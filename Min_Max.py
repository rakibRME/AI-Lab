import math
def MiniMax(node, move, pacMan):
    if move == 0 or not edges[node]:
        return leafNonde.get(node, 0)

    if pacMan:
        max_pacMan = -math.inf
        for i in edges[node]:
            pacMan = MiniMax(i, move - 1, False)
            max_pacMan = max(max_pacMan, pacMan)
        return max_pacMan
    else:
        min_ghost = math.inf
        for i in edges[node]:
            pacMan = MiniMax(i, move - 1, True)
            min_ghost = min(min_ghost, pacMan)
        return min_ghost

edges = {
    "0": ["1", "2"],
    "1": ["3", "4"],
    "2": ["5", "6"],
    "3": ["7", "8"],
    "4": ["9","10"],
    "5": ["11", "12"],
    "6": ["13", "14"],
    "7": [],
    "8": [],
    "9": [],
    "10": [],
    "11": [],
    "12": [],
    "13": [],
    "14": []
}

leafNonde = {
    "7": 1,
    "8": 1,
    "9": 2,
    "10": -3,
    "11": 5,
    "12": 7,
    "13": -2,
    "14": 2
}

root_node = "0"
level = 4

score = MiniMax(root_node, level, True)
print("Maximum Score", score)