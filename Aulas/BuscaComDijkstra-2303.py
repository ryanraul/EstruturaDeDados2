
class Grafo:
    
    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}
        
    def adiciona_vertice(self, valor):
        self.vertices.append(valor)
        self.arestas[valor] = []
        
    def adiciona_aresta(self, origem, destino, peso):
        
        if origem not in self.vertices:
            self.adiciona_vertice(origem)

        if destino not in self.vertices:
            self.adiciona_vertice(destino)
        
        self.arestas[origem].append(destino)
        self.pesos[(origem,destino)] = peso
        

def menor_distancia(vertices, distancias):
    
    menor_vertice = None
    menor_distancia = None
    
    for vertice in vertices:
        
        if menor_vertice is None or distancias[vertice] < menor_distancia:
            menor_vertice = vertice
            menor_distancia = distancias[vertice]
            
    return menor_vertice


def dijkstra(grafo, inicio):
    
    dist = {inicio:0}
    T = [inicio]
    P = []
    
    while len(T) > 0:
        
        # pega nos vertices de T, aquele que tem a menor distancia
        v = menor_distancia(T, dist)
        
        T.pop(T.index(v))
        P.append(v)
        
        for u in grafo.arestas[v]:
            
            if u in T:
                dist[u] = min(dist[u], dist[v] + grafo.pesos[(v,u)])
                
            elif u not in P:
                dist[u] = dist[v] + grafo.pesos[(v,u)]
                T.append(u)
                
    return dist


#####################

g = Grafo()

g.adiciona_aresta("S", "A", 1)
g.adiciona_aresta("S", "B", 5)
g.adiciona_aresta("A", "B", 2)
g.adiciona_aresta("A", "C", 2)
g.adiciona_aresta("A", "D", 1)
g.adiciona_aresta("B", "D", 2)
g.adiciona_aresta("C", "D", 3)
g.adiciona_aresta("C", "E", 1)
g.adiciona_aresta("D", "E", 2)

print(g.vertices)
print(g.arestas)
print(g.pesos)

distancias = dijkstra(g, 'S')

print(distancias)