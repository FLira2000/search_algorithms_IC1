class Busca:
    def __init__(self, nodes, grafo):
        self.nodes = nodes
        self.grafo = grafo

    def performar_busca_ordenada(self, inicio, end):
        nao_visitado = {n: float("inf") for n in self.nodes}
        nao_visitado[inicio] = 0
        visitado = {}
        pais = {}
        while nao_visitado:
            vertice_min = min(nao_visitado, key=nao_visitado.get)
            for neighbour, _ in self.grafo.get(vertice_min, {}).items():
                if neighbour in visitado:
                    continue
                new_distance = nao_visitado[vertice_min] + self.grafo[vertice_min].get(
                    neighbour, float("inf")
                )
                if new_distance < nao_visitado[neighbour]:
                    nao_visitado[neighbour] = new_distance
                    pais[neighbour] = vertice_min
            visitado[vertice_min] = nao_visitado[vertice_min]
            nao_visitado.pop(vertice_min)
            if vertice_min == end:
                break
        return visitado


def main():
    nodes = ("A", "B", "C", "D", "E", "F", "G")
    grafo = {
        "A": {"B": 9, "C": 5, "D": 13},
        "B": {"A": 9, "D": 3, "E": 10},
        "C": {"F": 12, "A": 5},
        "D": {"A": 13, "B": 3, "E": 6, "G": 14},
        "E": {"B": 10, "D": 6, "G": 7},
        "G": {"E": 7, "F": 10, "D": 14},
        "F": {"C": 12, "G": 10},
    }

    x = Busca(nodes, grafo)
    res = x.performar_busca_ordenada("A", "G")
    if res is None:
        print('Caminho não encontrado')
    else:
        print('Caminho encontrado')
        print(res)
