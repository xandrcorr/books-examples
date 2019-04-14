import time


def search_dist(graph, start, end):
    if start == end:
        return 0
    queue = graph[start]
    dist = 1
    while queue:
        next_queue = []
        for item in queue:
            if item == end:
                return dist
            next_queue.extend(graph[item])
        queue = next_queue
        dist += 1
    return dist


if __name__ == "__main__":
    graph = {}
    graph["cab"] = ["car", "cat"]
    graph["car"] = ["cat", "bar"]
    graph["cat"] = ["mat", "bat"]
    graph["mat"] = ["bat"]
    graph["bat"] = []
    graph["bar"] = ["bat"]
    result = search_dist(graph, "cab", "bat")
    print(result)