class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_vizinhos(self, v):
        return self.adjac_lis[v]

    def h(self, n):
        H = {
            "A": 24,
            "B": 15,
            "C": 22,
            "D": 12,
            "E": 7,
            "F": 7,
            "G": 0
        }
        return H[n]

    def a_estrela(self, inicio, fim):
        aberto_lst = set([inicio])
        fechado_lst = set([])
        inicio_todas_adjaca_nodes = {}
        inicio_todas_adjaca_nodes[inicio] = 0
        todas_adjac = {}
        todas_adjac[inicio] = inicio

        while len(aberto_lst) > 0:
            n = None
            for v in aberto_lst:
                if n is None or inicio_todas_adjaca_nodes[v] + self.h(
                    v
                ) < inicio_todas_adjaca_nodes[n] + self.h(n):
                    n = v

            if n is None:
                print("Caminho nao existe!")
                return None

            if n == fim:
                caminho_novo = []
                while todas_adjac[n] != n:
                    caminho_novo.append(n)
                    n = todas_adjac[n]
                caminho_novo.append(inicio)
                caminho_novo.reverse()
                print("Caminho encontrado: {}".format(caminho_novo))
                return caminho_novo

            for (m, weight) in self.get_vizinhos(n):
                if m not in aberto_lst and m not in fechado_lst:
                    aberto_lst.add(m)
                    todas_adjac[m] = n
                    inicio_todas_adjaca_nodes[m] = inicio_todas_adjaca_nodes[n] + weight

                else:
                    if (
                        inicio_todas_adjaca_nodes[m]
                        > inicio_todas_adjaca_nodes[n] + weight
                    ):
                        inicio_todas_adjaca_nodes[m] = (
                            inicio_todas_adjaca_nodes[n] + weight
                        )
                        todas_adjac[m] = n

                        if m in fechado_lst:
                            fechado_lst.remove(m)
                            aberto_lst.add(m)

            aberto_lst.remove(n)
            fechado_lst.add(n)

        print("Caminho nao existe!")
        return None


def main():
    nodes = {
        "A": [("B", 9), ("C", 5), ("D", 13)],
        "B": [("D", 3), ("E", 10)],
        "C": [("F", 12)],
        "D": [("E", 6), ("G", 14)],
        "E": [("G", 7)],
        "F": [("G", 10)],
    }
    grafo = Graph(nodes)
    grafo.a_estrela("A", "G")


if __name__ == "__main__":
    main()
