from numpy import inf

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


def BFS(G, s):
    
    arvore = []  # alteracao
    
    visitadosT = [s]
    
    distLambda = {}
    distLambda[s] = 0
    
    filaQ = [s]
    
    while len(filaQ) > 0:
        u = filaQ.pop(0)
        
        for v in G.arestas[u]:  # alteracao
            
            if v not in visitadosT:
                
                arvore.append((u,v)) # alteracao
                
                filaQ.append(v)
                visitadosT.append(v)
                
                distLambda[v] = distLambda[u] + 1
 
    return arvore


def menorLambda(TEMP, lb):
    
    menorVertice = None
    menorDistancia = inf
    
    for v in lb.keys():
        if v in TEMP and menorDistancia > lb[v]:
            menorDistancia = lb[v]
            menorVertice = v

    return menorVertice


def prim(G, s):
    
    lb = {}
    e  = {}
    
    for v in G.vertices:
        lb[v] = inf
        
    lb[s] = 0
    e[s] = None
    
    TEMP = G.vertices.copy()

    T = []
    
    while len(TEMP) > 0:
        
        # pegar um vertice v da TEMP onde lb(v) é o menor
        v = menorLambda(TEMP, lb)

        TEMP.remove(v)
        T.append(e[v])
        
        for u in G.arestas[v]:
            if u in TEMP and lb[u] > G.pesos[(v,u)]:
                lb[u] = G.pesos[(v,u)]
                e[u] = (v,u)
                
    return T, e

########

g = Grafo()

"""
g.adiciona_aresta("A", "B", 3)
g.adiciona_aresta("A", "C", 5)
g.adiciona_aresta("A", "D", 1)
g.adiciona_aresta("B", "E", 4)
g.adiciona_aresta("C", "E", 8)
g.adiciona_aresta("C", "D", 4)
g.adiciona_aresta("D", "F", 3)
g.adiciona_aresta("E", "F", 7)
"""

g.adiciona_aresta("Fallarbor", "Mauville", 19)
g.adiciona_aresta("Fallarbor", "Rustboro", 9)
g.adiciona_aresta("Fortree", "Lilycove", 7)
g.adiciona_aresta("Fortree", "Mauville", 9)
g.adiciona_aresta("Mauville", "Verdanturf", 2)
g.adiciona_aresta("Mauville", "Slateport", 8)
g.adiciona_aresta("Oldale", "Petalburg", 2)
g.adiciona_aresta("Petalburg", "Rustboro", 6)
g.adiciona_aresta("Rustboro", "Verdanturf", 4)
g.adiciona_aresta("Dewford", "Littleroot", 5)
g.adiciona_aresta("Dewford", "Pacifidlog", 16)
g.adiciona_aresta("Fortree", "Pacifidlog", 14)
g.adiciona_aresta("Lavaridge", "Mauville", 6)
g.adiciona_aresta("Lilycove", "Mauville", 14)
g.adiciona_aresta("Mauville", "Pacifidlog", 12)
g.adiciona_aresta("Mossdeep", "Pacifidlog", 14)
g.adiciona_aresta("Petalburg", "Verdanturf", 7)
g.adiciona_aresta("Dewford", "Petalburg", 9)
g.adiciona_aresta("Dewford", "Slateport", 20)
g.adiciona_aresta("Ever Grand", "Lilycove", 13)
g.adiciona_aresta("Ever Grand", "Pacifidlog", 15)
g.adiciona_aresta("Ever Grand", "Sootopolis", 12)
g.adiciona_aresta("Lilycove", "Mossdeep", 6)
g.adiciona_aresta("Lilycove", "Sootopolis", 6)
g.adiciona_aresta("Littleroot", "Oldale", 5)
g.adiciona_aresta("Mossdeep", "Sootopolis", 8)
g.adiciona_aresta("Pacifidlog", "Slateport", 11)
g.adiciona_aresta("Pacifidlog", "Sootopolis", 17)

# Total somando todas as arestas

sum = 0
for p in g.pesos.values():
    sum += p
    
print(sum)


## Exercicio 1 - Árvore geradora qualquer (BFS adaptada)

arvore = BFS(g,'Fallarbor')
print(arvore)

# Total das arestas
sum = 0
for e in arvore:
    sum += g.pesos[e]
    
print(sum)


## Exercicio 2 - Árvore geradora mínima (Prim)

T, e = prim(g, 'Fallarbor')
print(T)

sum = 0
for e in T[1:]:
    sum += g.pesos[e]
    
print(sum)