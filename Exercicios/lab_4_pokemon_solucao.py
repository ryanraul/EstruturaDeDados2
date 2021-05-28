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
        self.arestas[destino].append(origem)
        
        self.pesos[(origem,destino)] = peso
        self.pesos[(destino,origem)] = peso
        
        
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
    caminho = {inicio:[inicio]}
    
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
                if dist[u] > dist[v] + grafo.pesos[(v,u)]:
                    dist[u] = dist[v] + grafo.pesos[(v,u)]
                    caminho[u] = caminho[v] + [u]
                

            elif u not in P:

                # encontrou um novo no que nao esta nem em T nem em P
                dist[u] = dist[v] + grafo.pesos[(v,u)]
                caminho[u] = caminho[v] + [u]
                T.append(u)

    return dist, caminho
    
    
def menorRota(mapa, origem, destino, usaAereo, usaAquatico):
    
    if usaAquatico:
        mapa.adiciona_aresta("Dewford", "Petalburg", 9)
        mapa.adiciona_aresta("Dewford", "Slateport", 20)
        mapa.adiciona_aresta("Ever Grand", "Lilycove", 13)
        mapa.adiciona_aresta("Ever Grand", "Pacifidlog", 15)
        mapa.adiciona_aresta("Ever Grand", "Sootopolis", 12)
        mapa.adiciona_aresta("Lilycove", "Mossdeep", 6)
        mapa.adiciona_aresta("Lilycove", "Sootopolis", 6)
        mapa.adiciona_aresta("Littleroot", "Oldale", 5)
        mapa.adiciona_aresta("Mossdeep", "Sootopolis", 8)
        mapa.adiciona_aresta("Pacifidlog", "Slateport", 11)
        mapa.adiciona_aresta("Pacifidlog", "Sootopolis", 17)

        
    if usaAereo:
        mapa.adiciona_aresta("Dewford", "Littleroot", 5)
        mapa.adiciona_aresta("Dewford", "Pacifidlog", 16)
        mapa.adiciona_aresta("Fortree", "Pacifidlog", 14)
        mapa.adiciona_aresta("Lavaridge", "Mauville", 6)
        mapa.adiciona_aresta("Lilycove", "Mauville", 14)
        mapa.adiciona_aresta("Mauville", "Pacifidlog", 12)
        mapa.adiciona_aresta("Mossdeep", "Pacifidlog", 14)
        mapa.adiciona_aresta("Petalburg", "Verdanturf", 7)
        
    distancias, caminho = dijkstra(mapa, origem)
    
    return distancias, caminho
    
    
    

###############

g = Grafo()

# rotas terrestres

g.adiciona_aresta("Fallarbor", "Mauville", 19)
g.adiciona_aresta("Fallarbor", "Rustboro", 9)
g.adiciona_aresta("Fortree", "Lilycove", 7)
g.adiciona_aresta("Fortree", "Mauville", 9)
g.adiciona_aresta("Mauville", "Verdanturf", 2)
g.adiciona_aresta("Mauville", "Slateport", 8)
g.adiciona_aresta("Oldale", "Petalburg", 2)
g.adiciona_aresta("Petalburg", "Rustboro", 6)
g.adiciona_aresta("Rustboro", "Verdanturf", 4)


dist, caminho = menorRota(  mapa=g,
                            origem="Petalburg", 
                            destino="Lilycove",
                            usaAereo=True, 
                            usaAquatico=False)
                            
print(dist)

for destino in caminho.keys():
    print(caminho[destino])