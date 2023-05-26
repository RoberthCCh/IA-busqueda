from collections import deque


def buscar_solucion():
    # Estado inicial: (0, 0)
    estado_inicial = (0, 0)

    # Estados finales: todos los estados de la forma (2, y)
    estados_finales = [(2, y) for y in range(4)]

    # Operadores
    operadores = [
        ("Llenar jarra de 3", lambda x, y: (x, 3)),
        ("Llenar jarra de 4 con jarra de 3", lambda x,
         y: (4, x + y - 4) if x + y > 4 else None),
        ("Vaciar jarra de 3 en jarra de 4", lambda x,
         y: (x + y, 0) if x + y <= 4 else None),
        ("Llenar jarra de 4", lambda x, y: (4, y)),
        ("Vaciar jarra de 4", lambda x, y: (0, y)),
        ("Llenar jarra de 3 con jarra de 4", lambda x, y: (
            x - (3 - y), 3) if x + y > 3 and y < 3 else None),
        ("Vaciar jarra de 3", lambda x, y: (x, 0)),
        ("Vaciar jarra de 4 en jarra de 3", lambda x,
         y: (0, x + y) if x + y <= 3 else None)
    ]

    # Inicializar la cola de búsqueda con el estado inicial
    cola = deque([(estado_inicial, [])])
    visitados = set()

    while cola:
        estado_actual, acciones = cola.popleft()

        if estado_actual in estados_finales:
            # Se encontró una solución
            return acciones

        visitados.add(estado_actual)

        for nombre_operador, operador in operadores:
            nuevo_estado = operador(*estado_actual)

            if nuevo_estado is not None and nuevo_estado not in visitados:
                nueva_accion = acciones + [nombre_operador]
                cola.append((nuevo_estado, nueva_accion))

    # No se encontró una solución
    return None


# Ejecutar la búsqueda de la solución
solucion = buscar_solucion()

if solucion:
    print("Solución encontrada:")
    for i, accion in enumerate(solucion):
        print(f"Paso {i+1}: {accion}")
else:
    print("No se encontró una solución.")
