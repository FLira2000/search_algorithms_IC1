class Grafo:
    def __init__(self, grafo_dicio=None, direcionado=True):
        self.grafo_dicio = grafo_dicio or {}
        self.direcionado = direcionado
        if not direcionado:
            self.transforma_arvore()

    def transforma_arvore(self):
        for a in list(self.grafo_dicio.keys()):
            for (b, dist) in self.grafo_dicio[a].items():
                self.grafo_dicio.setdefault(b, {})[a] = dist

    def relacao(self, A, B, distance=1):
        self.grafo_dicio.setdefault(A, {})[B] = distance
        if not self.direcionado:
            self.grafo_dicio.setdefault(B, {})[A] = distance

    def get(self, a, b=None):
        relacoes = self.grafo_dicio.setdefault(a, {})
        if b is None:
            return relacoes
        else:
            return relacoes.get(b)

    def nodes(self):
        s1 = set([k for k in self.grafo_dicio.keys()])
        s2 = set([k2 for v in self.grafo_dicio.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

class Node:
    def __init__(self, nome:str, pais:str):
        self.nome = nome
        self.pais = pais
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, outro):
        return self.nome == outro.nome

    def __lt__(self, outro):
        return self.f < outro.f

    def __repr__(self):
        return ('({0},{1})'.format(self.posicao, self.f))


def gulosa(grafo, heuristica, inicio, fim):
    aberto = []
    fechado = []

    node_inicial = Node(inicio, None)
    node_final = Node(fim, None)

    aberto.append(node_inicial)

    while len(aberto) > 0:
        aberto.sort()
        node_atual = aberto.pop(0)
        # print(grafo.get(node_atual.nome))
        fechado.append(node_atual)
        if node_atual == node_final:
            caminho = []
            while node_atual != node_inicial:
                caminho.append(node_atual.nome + ': ' + str(node_atual.g))
                node_atual = node_atual.pais
            caminho.append(node_inicial.nome + ': ' + str(node_inicial.g))
            return caminho[::-1]

        vizinhos = grafo.get(node_atual.nome)
        for key, value in vizinhos.items():
            vizinho = Node(key, node_atual)
            if(vizinho in fechado):
                continue
            vizinho.g = node_atual.g + grafo.get(node_atual.nome, vizinho.nome)
            vizinho.h = heuristica.get(vizinho.nome)
            vizinho.f = vizinho.h
            print(grafo.get(vizinho.nome))
            if add_em_aberto(aberto, vizinho) is True:
                aberto.append(vizinho)

    return None


def add_em_aberto(aberto, vizinho):
    for node in aberto:
        if (vizinho == node and vizinho.f >= node.f):
            return False
    return True


def main():
    grafo = Grafo()
    grafo.relacao('A', 'B', 9)
    grafo.relacao('A', 'C', 5)
    grafo.relacao('A', 'D', 13)
    grafo.relacao('B', 'D', 3)
    grafo.relacao('B', 'E', 10)
    grafo.relacao('C', 'F', 12)
    grafo.relacao('D', 'E', 6)
    grafo.relacao('D', 'G', 14)
    grafo.relacao('E', 'G', 7)
    grafo.relacao('F', 'G', 10)
    grafo.transforma_arvore()
    heuristica = {}
    heuristica['A'] = 24
    heuristica['B'] = 13
    heuristica['C'] = 15
    heuristica['D'] = 7
    heuristica['E'] = 10
    heuristica['F'] = 10
    heuristica['G'] = 0
    caminho = gulosa(grafo, heuristica, 'A', 'G')
    print("Melhor caminho:", caminho)


if '__name__' == '__main__':
    main()
