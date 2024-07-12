#astar
def astar(start, stop):
    open_set, closed_set = {start}, set()
    g, parents = {start: 0}, {start: start}
    heuristic = lambda n: {'A': 10, 'B': 8, 'C': 5, 'D': 7, 'E': 3, 'F': 6, 'G': 5, 'H': 4, 'I': 1, 'J': 0}[n]

    while open_set:
        n = min(open_set, key=lambda v: g[v] + heuristic(v))

        if n == stop:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print('Path found:', path)
            return path

        open_set.remove(n)
        closed_set.add(n)

        for m, weight in graph_nodes.get(n, []):
            if m in closed_set:
                continue

            tentative_g = g[n] + weight

            if m not in open_set or tentative_g < g[m]:
                g[m], parents[m] = tentative_g, n
                open_set.add(m)

    print('Path doesn\'t exist')
    return None

graph_nodes = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)]
}

astar('A', 'J')


# Path found: ['A', 'F', 'G', 'I', 'J']
# ['A', 'F', 'G', 'I', 'J']