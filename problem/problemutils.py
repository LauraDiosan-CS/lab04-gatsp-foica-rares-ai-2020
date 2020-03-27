def pathCost(path, graph):
    cost = 0
    for i in range(1, len(path)):
        cost += graph.weight(path[i - 1], path[i])
    # account for the edge that returns back to the starting node
    cost += graph.weight(path[-1], path[0])
    return cost

def translateNodes(nodes, step):
    return [x+step for x in nodes]