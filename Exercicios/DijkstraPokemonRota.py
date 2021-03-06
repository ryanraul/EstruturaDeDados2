
class Grafo:
    
    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}
        self.tipos = {}
        
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
        self.tipos[(origem, destino)] = tipo
        

def busca_menor_distancia(vertices, distancias):
    
    menor_vertice = None
    menor_distancia = None
    
    for vertice in vertices:
        
        if menor_vertice is None or distancias[vertice] < menor_distancia:
            menor_vertice = vertice
            menor_distancia = distancias[vertice]
            
    return menor_vertice


def dijkstra(grafo, inicio, usarAereo, usarAquatico):
    
    dist = {inicio:0}
    T = [inicio]
    P = []
    
    while len(T) > 0:
        
        v = busca_menor_distancia(T, dist)
        
        T.pop(T.index(v))
        P.append(v)
        
        for u in grafo.arestas[v]:
            
            if grafo.tipos[(v, u)] == "V" and usarAereo == False:
                continue
            if grafo.tipos[(v, u)] == "A" and usarAquatico == False:
                continue

            if u in T:
                dist[u] = min(dist[u], dist[v] + grafo.pesos[(v,u)])
                
            elif u not in P:
                dist[u] = dist[v] + grafo.pesos[(v,u)]
                T.append(u)
                
    return dist


def MenorRota(mapa, origem, destino, usarAereo, usarAquatico):
    distancias = dijkstra(mapa, destino, usarAereo, usarAquatico)
    if origem not in distancias:
        return "Não há a rota para esse local"
    rota_auxiliar = [origem]
    menor_rota = []
    distancia_percorrer = distancias[origem]

    while destino not in menor_rota or not rota_auxiliar:        

        vertice_origem = busca_menor_distancia(rota_auxiliar, distancias)

        rota_auxiliar.pop(rota_auxiliar.index(vertice_origem))
        menor_rota.append(vertice_origem)

        menor_vertice = None
        menor_distancia = None
        for vertice_destino in mapa.arestas[vertice_origem]: 
            if vertice_destino not in distancias:
                continue
            if menor_vertice is None or distancias[vertice_origem] < menor_distancia:
                if mapa.tipos[(vertice_origem, vertice_destino)] == "V" and usarAereo == False:
                    continue
                if mapa.tipos[(vertice_origem, vertice_destino)] == "A" and usarAquatico == False:
                    continue
                menor_vertice = vertice_destino
                menor_distancia = distancias[vertice_destino]
        rota_auxiliar.append(menor_vertice)

    return menor_rota


g = Grafo()

Terrestre, Voador, Aquatico = "T", "V", "A"
g.adiciona_aresta("Rustboro", "Verdanturf", 4, Terrestre)
g.adiciona_aresta("Rustboro", "Fallarbor", 9, Terrestre)
g.adiciona_aresta("Rustboro", "Petalburg", 6, Terrestre)
g.adiciona_aresta("Verdanturf", "Mauville", 2, Terrestre)
g.adiciona_aresta("Verdanturf", "Rustboro", 4, Terrestre)
g.adiciona_aresta("Verdanturf", "Petalburg", 7, Voador)
g.adiciona_aresta("Fallarbor", "Mauville", 19, Terrestre)
g.adiciona_aresta("Fallarbor", "Rustboro", 9, Terrestre)
g.adiciona_aresta("Petalburg", "Verdanturf", 7, Voador)
g.adiciona_aresta("Petalburg", "Rustboro", 6, Terrestre)
g.adiciona_aresta("Petalburg", "Oldale", 2, Terrestre)
g.adiciona_aresta("Petalburg", "Dewford", 9, Aquatico)
g.adiciona_aresta("Mauville", "Verdanturf", 2, Terrestre)
g.adiciona_aresta("Mauville", "Fallarbor", 19, Terrestre)
g.adiciona_aresta("Mauville", "Slateport", 8, Terrestre)
g.adiciona_aresta("Mauville", "Fortree", 9, Terrestre)
g.adiciona_aresta("Mauville", "Lavaridge", 6, Voador)
g.adiciona_aresta("Mauville", "Pacifidlog", 12, Voador)
g.adiciona_aresta("Mauville", "Lavaridge", 6, Voador)
g.adiciona_aresta("Lavaridge", "Mauville", 14, Voador)
g.adiciona_aresta("Oldale", "Littleroot", 5, Terrestre)
g.adiciona_aresta("Oldale", "Petalburg", 2, Terrestre)
g.adiciona_aresta("Littleroot", "Oldale", 5, Terrestre)
g.adiciona_aresta("Littleroot", "Dewford", 5, Voador)
g.adiciona_aresta("Dewford", "Slateport", 20, Aquatico)
g.adiciona_aresta("Dewford", "Petalburg", 9, Aquatico)
g.adiciona_aresta("Dewford", "Littleroot", 5, Voador)
g.adiciona_aresta("Dewford", "Pacifidlog", 16, Voador)
g.adiciona_aresta("Slateport", "Pacifidlog", 11, Aquatico)
g.adiciona_aresta("Slateport", "Dewford", 20, Aquatico)
g.adiciona_aresta("Slateport", "Mauville", 8, Terrestre)
g.adiciona_aresta("Fortree", "Lilycove", 7, Terrestre)
g.adiciona_aresta("Fortree", "Pacifidlog", 14, Voador)
g.adiciona_aresta("Fortree", "Mauville", 9, Terrestre)
g.adiciona_aresta("Pacifidlog", "Mossdeep", 14, Voador)
g.adiciona_aresta("Pacifidlog", "Mauville", 12, Voador)
g.adiciona_aresta("Pacifidlog", "Dewford", 16, Voador)
g.adiciona_aresta("Pacifidlog", "Slateport", 11, Aquatico)
g.adiciona_aresta("Pacifidlog", "Fortree", 14, Voador)
g.adiciona_aresta("Pacifidlog", "Sootopolis", 17, Aquatico)
g.adiciona_aresta("Pacifidlog", "EverGrand", 15, Aquatico)
g.adiciona_aresta("EverGrand", "Pacifidlog", 15, Aquatico)
g.adiciona_aresta("EverGrand", "Lilycove", 13, Aquatico)
g.adiciona_aresta("EverGrand", "Sootopolis", 12, Aquatico)
g.adiciona_aresta("Lilycove", "Sootopolis", 6, Aquatico)
g.adiciona_aresta("Lilycove", "Fortree", 7, Terrestre)
g.adiciona_aresta("Lilycove", "Mauville", 14, Voador)
g.adiciona_aresta("Lilycove", "Mossdeep", 6, Aquatico)
g.adiciona_aresta("Lilycove", "EverGrand", 13, Aquatico)
g.adiciona_aresta("Mossdeep", "Sootopolis", 8, Aquatico)
g.adiciona_aresta("Mossdeep", "Pacifidlog", 14, Voador)
g.adiciona_aresta("Mossdeep", "Lilycove", 6, Aquatico)
g.adiciona_aresta("Sootopolis", "EverGrand", 12, Terrestre)
g.adiciona_aresta("Sootopolis", "Pacifidlog", 17, Aquatico)
g.adiciona_aresta("Sootopolis", "Lilycove", 6, Aquatico)
g.adiciona_aresta("Sootopolis", "Mossdeep", 8, Aquatico)

#print(g.vertices)
#print("\n\n")
#print(g.arestas)
#print("\n\n")
#print(g.pesos)
#print("\n\n")
#print(g.tipos)

#distancias = dijkstra(g, origem, False, False)
#print(distancias)

origem = 'Lilycove'
destino = 'Pacifidlog'
usarAereo = False
usarAquatico = True

menorRota = MenorRota(g, origem, destino, usarAereo, usarAquatico)
print(menorRota)