from collections import deque


def bfs(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)

    while queue:
        (vertex, path) = queue.popleft()

        if vertex == end:
            return path

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))


# Ejemplo de uso:
graph = {
    'A': ['B', 'C', 'Z'],
    'B': ['A', 'G', 'S', 'H'],
    'C': ['D'],
    'D': ['O', 'J'],
    'E': ['X', 'P'],
    'G': ['B', 'R', 'L'],
    'H': ['B', 'J', 'V', 'R'],
    'I': ['P', 'O'],
    'J': ['H', 'D'],
    'L': ['T', 'G'],
    'M': ['N', 'Y', 'X'],
    'N': ['M'],
    'O': ['O', 'D', 'S', 'I'],
    'P': ['E', 'I', 'Z'],
    'R': ['G', 'U', 'H'],
    'S': ['B', 'O'],
    'T': ['M', 'L'],
    'U': ['R'],
    'V': ['H'],
    'X': ['M', 'Y'],
    'Y': ['M', 'X'],
    'Z': ['P', 'A']

}
start = 'B'
end = 'P'
path = bfs(graph, start, end)
print(path)
