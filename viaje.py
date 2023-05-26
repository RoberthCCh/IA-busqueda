from collections import deque


def buscar_solucion():
    # Estado inicial: Sevilla
    estado_inicial = "Sevilla"

    # Estado final: Almería
    estado_final = "Almería"

    # Operadores
    operadores = {
        "Ir a Almería": ["Cádiz"],
        "Ir a Cádiz": ["Sevilla", "Málaga"],
        "Ir a Córdoba": ["Sevilla", "Granada"],
        "Ir a Granada": ["Córdoba", "Jaén"],
        "Ir a Huelva": ["Sevilla"],
        "Ir a Jaén": ["Granada"],
        "Ir a Málaga": ["Cádiz", "Córdoba"],
        "Ir a Sevilla": ["Cádiz", "Huelva", "Córdoba"]
    }

    # Inicializar la cola de búsqueda con el estado inicial
    cola = deque([(estado_inicial, [])])
    visitados = set()

    while cola:
        estado_actual, acciones = cola.popleft()

        if estado_actual == estado_final:
            # Se encontró una solución
            return acciones

        visitados.add(estado_actual)

        for accion, destinos in operadores.items():
            if estado_actual in destinos:
                nuevo_estado = accion[5:]  # Obtener la capital destino
                if nuevo_estado not in visitados:
                    nueva_accion = acciones + [accion]
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
