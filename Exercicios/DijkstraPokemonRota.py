
class Grafo:
    
    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}
        
    def adiciona_vertice(self, valor):
        self.vertices.append(valor)
        self.arestas[valor] = []
        
    def adiciona_aresta(self, origem, destino, peso, tipo):
        
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

Terrestre, Voador, Aquatico = "T", "V", "A"

g.adiciona_aresta("Rustboro", "Verdanturf", 4, Terrestre)
g.adiciona_aresta("Rustboro", "Fallarbor", 9, Terrestre)
g.adiciona_aresta("Rustboro", "Petalburg", 6, Terrestre)
g.adiciona_aresta("Verdanturf", "Mauville", 2, Terrestre)
g.adiciona_aresta("Verdanturf", "Petalburg", 7, Voador)
g.adiciona_aresta("Fallarbor", "Mauville", 19, Terrestre)
g.adiciona_aresta("Petalburg", "Oldale", 2, Terrestre)
g.adiciona_aresta("Petalburg", "Dewford", 9, Aquatico)
g.adiciona_aresta("Mauville", "Slateport", 8, Terrestre)
g.adiciona_aresta("Mauville", "Fortree", 9, Terrestre)
g.adiciona_aresta("Mauville", "Lavaridge", 6, Voador)
g.adiciona_aresta("Mauville", "Pacifidlog", 12, Voador)
g.adiciona_aresta("Mauville", "Lilycove", 14, Voador)
g.adiciona_aresta("Oldale", "Littleroot", 5, Terrestre)
g.adiciona_aresta("Dewford", "Slateport", 20, Aquatico)
g.adiciona_aresta("Dewford", "Littleroot", 5, Voador)
g.adiciona_aresta("Dewford", "Pacifidlog", 16, Voador)
g.adiciona_aresta("Slateport", "Pacifidlog", 11, Aquatico)
g.adiciona_aresta("Fortree", "Lilycove", 7, Terrestre)
g.adiciona_aresta("Fortree", "Pacifidlog", 14, Voador)
g.adiciona_aresta("Pacifidlog", "Mossdeep", 14, Voador)
g.adiciona_aresta("Pacifidlog", "Sootopolis", 17, Aquatico)
g.adiciona_aresta("Pacifidlog", "EverGrand", 15, Aquatico)
g.adiciona_aresta("Lilycove", "Sootopolis", 6, Aquatico)
g.adiciona_aresta("Lilycove", "Mossdeep", 6, Aquatico)
g.adiciona_aresta("Lilycove", "EverGrand", 13, Aquatico)
g.adiciona_aresta("Mossdeep", "Sootopolis", 8, Aquatico)
g.adiciona_aresta("Sootopolis", "EverGrand", 12, Terrestre)


print(g.vertices)
print("\n\n")
print(g.arestas)
print("\n\n")
print(g.pesos)

distancias = dijkstra(g, 'Rustboro')

#print(distancias)