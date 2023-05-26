def es_estado_valido(estado):
    if (estado[1] == estado[2] and estado[0] != estado[1]) or (estado[2] == estado[3] and estado[0] != estado[2]):
        return False
    return True


def es_estado_final(estado):
    return estado == ('d', 'd', 'd', 'd')


def generar_nuevos_estados(estado_actual):
    nuevos_estados = []

    for i in range(4):
        if estado_actual[i] == estado_actual[0]:
            nuevo_estado = list(estado_actual)
            nuevo_estado[0] = 'i' if estado_actual[0] == 'd' else 'd'
            nuevo_estado[i] = 'i' if estado_actual[i] == 'd' else 'd'
            nuevos_estados.append(tuple(nuevo_estado))

    return nuevos_estados


def resolver_problema_granjero():
    estados = [
        ('i', 'i', 'i', 'i'),
        ('i', 'i', 'i', 'd'),
        ('i', 'i', 'd', 'i'),
        ('i', 'i', 'd', 'd'),
        ('i', 'd', 'i', 'i'),
        ('i', 'd', 'i', 'd'),
        ('i', 'd', 'd', 'i'),
        ('i', 'd', 'd', 'd'),
        ('d', 'i', 'i', 'i'),
        ('d', 'i', 'i', 'd'),
        ('d', 'i', 'd', 'i'),
        ('d', 'i', 'd', 'd'),
        ('d', 'd', 'i', 'i'),
        ('d', 'd', 'i', 'd'),
        ('d', 'd', 'd', 'i'),
        ('d', 'd', 'd', 'd')
    ]

    for estado_inicial in estados:
        visitados = set()
        camino_inicial = [estado_inicial]
        solucion = resolver_problema_granjero_recursivo(
            estado_inicial, visitados, camino_inicial)

        if solucion is None:
            print(
                f"No se encontró solución para el estado inicial {estado_inicial}")
        else:
            print(
                f"Solución encontrada para el estado inicial {estado_inicial}:")
            for i, estado in enumerate(solucion):
                print(f"Paso {i+1}: {estado}")
        print()


def resolver_problema_granjero_recursivo(estado_actual, visitados, camino):
    if es_estado_final(estado_actual):
        return camino

    visitados.add(estado_actual)

    nuevos_estados = generar_nuevos_estados(estado_actual)

    for nuevo_estado in nuevos_estados:
        if nuevo_estado not in visitados and es_estado_valido(nuevo_estado):
            nuevo_camino = camino + [nuevo_estado]
            solucion = resolver_problema_granjero_recursivo(
                nuevo_estado, visitados, nuevo_camino)
            if solucion is not None:
                return solucion

    return None


# Resolver el problema del granjero para los 16 estados posibles
resolver_problema_granjero()
