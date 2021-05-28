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
    
    menor_vertice   = None
    menor_distancia = None
    
    for vertice in vertices:
    
        if menor_vertice is None or distancias[vertice] < menor_distancia:
            menor_vertice = vertice
            menor_distancia = distancias[vertice]
            
    return menor_vertice


def dijkstra(grafo, inicio):
    
    dist = {inicio:0} # -> {'S':0}
    
    T = [inicio] # -> temporario
    P = []       # -> permanente
    
    while len(T) > 0:
        
        # retorna o vertice de menor distancia entre aqueles que estao em T
        v = menor_distancia(T, dist)
        
        T.pop(T.index(v))
        P.append(v)
        
        for u in grafo.arestas[v]:
            
            if u in T:
                
                # considera a menor distancia entre:
                # - a distancia que ja existia pra u
                # - a distancia do caminho atual de v -> u
                dist[u] = min(dist[u], dist[v] + grafo.pesos[(v,u)])

            elif u not in P:

                # encontrou um novo no que nao esta nem em T nem em P
                dist[u] = dist[v] + grafo.pesos[(v,u)]
                T.append(u)

    return dist

###############

# Qual é a pressão inicial que deve ser aplicada
#         para todas as casas serem abastecidas?

g = Grafo()

g.adiciona_aresta('principal', 'braco1', 8)
g.adiciona_aresta('braco1', 'casa1', 4)
g.adiciona_aresta('braco1', 'casa2', 5)
g.adiciona_aresta('braco1', 'braco2', 8)
#g.adiciona_aresta('braco2', 'braco3', 8)
g.adiciona_aresta('braco2', 'casa4', 4)
g.adiciona_aresta('braco2', 'casa5', 4)
g.adiciona_aresta('braco3', 'casa4', 1)
g.adiciona_aresta('braco3', 'casa3', 6)

distancias = dijkstra(g, 'principal')

print(distancias)

print('Vertices com distancia calculada:', len(distancias))
print('Vertices inclusos no grafo:', len(g.vertices))

nao_comunicantes = set(g.vertices) - set(distancias.keys())

print("Vértices não-comunicantes:", nao_comunicantes)