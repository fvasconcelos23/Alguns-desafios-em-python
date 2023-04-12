def criar_grafo(conexoes):
    grafo = {}
    for conexao in conexoes:
        u, v = conexao
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append(v)
        grafo[v].append(u)
    return grafo


def contar_usuarios(conexoes, n):
    grafo = {}
    for i in range(1, n+1):
        grafo[i] = []
    for conexao in conexoes:
        u, v = conexao
        grafo[u].append(v)
        grafo[v].append(u)
    resultados = []
    for i in range(1, n+1):
        visitados = busca_profundidade(grafo, i)
        if visitados != 0:
            resultados.append(visitados)
    return resultados


def busca_profundidade(grafo, vertice_inicial):
    visitados = set()
    pilha = [vertice_inicial]
    while pilha:
        u = pilha.pop()
        if u not in visitados:
            visitados.add(u)
            for v in grafo[u]:
                pilha.append(v)

    return len(visitados)


n, m = map(int, input().split())
conexoes = [tuple(map(int, input().split())) for _ in range(m)]
resultado = contar_usuarios(conexoes, n)
print(" ".join(map(str, resultado)))
