def bfs(grafo, vertice_inicial, tamanho_maximo):
    visitados = []
    fila = []

    visitados.append(vertice_inicial)
    fila.append(vertice_inicial)

    while fila and len(visitados) < tamanho_maximo:
        vertice_atual = fila.pop(0)

        for vertice_adjacente in grafo[vertice_atual]:
            if vertice_adjacente not in visitados:
                visitados.append(vertice_adjacente)
                fila.append(vertice_adjacente)
                if len(visitados) >= tamanho_maximo:
                    break

    return visitados


def boost(n, u, b, grafo):

    max_nivel = len(grafo[u]) + (b // 5.25) + 1

    visitados = bfs(grafo, u, max_nivel)

    visitados.pop(0)

    return visitados


n = int(input())
u = input()
b = float(input())

grafo = {}
for _ in range(n):
    line = input().split(' : ')
    user_id = line[0]
    seguidores = line[1].split()
    grafo[user_id] = seguidores

alcançados = boost(n, u, b, grafo)

print(alcançados)
