'''Dijkstra's algorithm to find the shortest path in a graph.'''

graph = {'start': {'a': 6, 'b': 2},  'a': {'fin': 1},
         'b': {'a': 3, 'fin': 5},    'fin': {}}
infinity = float('inf')
costs = {'a': 6, 'b': 2, 'fin': infinity}
parents = {'a': 'start', 'b': 'start', 'fin': None}

processed = []


def find_lowest_cost_node(costs):
    '''Find the lowest cost node.'''
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra():
    '''Dijkstra's algorithm to find the shortest path in a graph.'''
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


dijkstra()
print('Cost from the start to each node:', costs)
