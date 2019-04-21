import time


def init_graph():
    graph = {}
    graph["start"] = {
        "a": 2,
        "b": 4
    }
    graph["a"] = {
        "c": 6
    }
    graph["b"] = {
        "c": 3,
        "d": 7
    }
    graph["c"] = {
        "d": 3,
        "end": 7
    }
    graph["d"] = {
        "end": 5
    }
    return graph

def solve_dijkstra(graph, start, end) -> ([], float):
    costs = graph[start]
    parents = { node: start for node in graph[start].keys() }
    processed = []
    node = get_lowest_cost_node(costs, processed)
    while node and node != end:
        neighbors = graph[node]
        for n, c in neighbors.items():
            new_cost = costs[node] + c
            cost = costs.setdefault(n, float("inf"))
            if new_cost < cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = get_lowest_cost_node(costs, processed)
    path = get_parent_chain(parents, end)
    return path, costs[end]

def get_lowest_cost_node(costs_dict, processed):
    min_cost = float("inf")
    min_node = None
    for node, cost in costs_dict.items():
        if cost < min_cost and node not in processed:
            min_cost = cost
            min_node = node
    return min_node

def get_parent_chain(parent_dict, node):
    if node in parent_dict.keys():
        return "{0}-{1}".format(get_parent_chain(parent_dict, parent_dict.get(node)), node)
    return node

if __name__ == "__main__":
    graph = init_graph()
    path, length = solve_dijkstra(graph, "start", "end")
    print("Min path: {0} | Length: {1}".format(path, length))
