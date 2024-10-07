def astar(start, goal, tree, heus):

    list = [(start, 0)]

    origin = {}

    gcost = {start: 0}

    while list:

        list.sort(key=lambda x: gcost[x[0]] + heus[x[0]])

        current_node, current_cost = list.pop(0)

        if current_node == goal:
            return new_Path(origin, start, goal)

        for neighbor, cost in tree[current_node]:
            new_cost = gcost[current_node] + cost


            if neighbor not in gcost or new_cost < gcost[neighbor]:
                gcost[neighbor] = new_cost
                list.append((neighbor, new_cost))
                origin[neighbor] = current_node

    return None

def new_Path(origin, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(origin[path[-1]])
    return path[::-1]  # reverse the path

tree = {
    'S': [('B', 3), ('A', 2), ('C', 5)],
    'A': [('C', 3), ('G', 2)],
    'B': [('D', 4),('A',4), ('E', 5),],
    'C': [('G', 4), ('H', 3)],
    'G': [('D', 3)],
    'H': [('D', 6)],
    'E': [('F', 5)],
    'D': [('E', 2),('F',3)]
}

heus = {
    'S': 10,
    'A': 8,
    'B': 9,
    'C': 7,
    'D': 4,
    'E': 3,
    'F': 0,
    'G': 6,
    'H': 6
}

path = astar('S', 'F', tree, heus)
print("Optimal path:", path)