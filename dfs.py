def dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path += [start]

    if start == end:
        return path

    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path)
            if new_path is not None:
                return new_path

    return None


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
path = dfs(graph, start, end)
print(path)
