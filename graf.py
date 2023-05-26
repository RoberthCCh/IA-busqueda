import tkinter as tk
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

    return None


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


def find_path():
    start = start_node_entry.get()
    end = end_node_entry.get()

    path_bfs = bfs(graph, start, end)
    path_dfs = dfs(graph, start, end)

    bfs_result_label.config(
        text="Camino encontrado con Anchura (BFS): " + str(path_bfs))
    dfs_result_label.config(
        text="Camino encontrado con Profundiad (DFS): " + str(path_dfs))


# Define el grafo
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

# Crea la ventana de la interfaz gráfica
window = tk.Tk()
window.title("BUSQUEDA DFS & BFS")

# Crea los widgets de la interfaz gráfica
start_node_label = tk.Label(window, text="Nodo Inicial:")
start_node_entry = tk.Entry(window)
end_node_label = tk.Label(window, text="Nodo Final:")
end_node_entry = tk.Entry(window)
find_path_button = tk.Button(
    window, text="BUSCAR CAMINO", command=find_path)
bfs_result_label = tk.Label(window, text="")
dfs_result_label = tk.Label(window, text="")

# Acomoda los widgets en la ventana
start_node_label.grid(row=0, column=0)
start_node_entry.grid(row=0, column=1)
end_node_label.grid(row=1, column=0)
end_node_entry.grid(row=1, column=1)
find_path_button.grid(row=2, column=0, columnspan=2)
bfs_result_label.grid(row=3, column=0, columnspan=2)
dfs_result_label.grid(row=4, column=0, columnspan=2)

# Inicia el bucle principal de la ventana
window.mainloop()
