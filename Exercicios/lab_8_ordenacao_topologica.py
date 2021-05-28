from numpy import inf

class Grafo:
    
    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}
        self.d_in = {} # alteracao
        
    def adiciona_aresta(self, origem, destino, peso):
        
        if origem not in self.vertices:
            self.adiciona_vertice(origem)
            self.d_in[origem] = 0   # alteracao
            
        if destino not in self.vertices:
            self.adiciona_vertice(destino)
            self.d_in[destino] = 0   # alteracao
        
        self.arestas[origem].append(destino)
        
        self.d_in[destino] += 1   # alteracao
        
        self.pesos[(origem,destino)] = peso
        
    def adiciona_vertice(self, valor):
        
        self.vertices.append(valor)
        self.arestas[valor] = []
        



def khan(G):
    
    Q = []
    ordem = []  # variavel f do algoritmo
    
    # linha 1 do algoritmo resolvido na classe
    
    for v in G.vertices: # linhas 2 e 3
        if G.d_in[v] == 0:
            Q.append(v)
    
    while len(Q) > 0:   # linha 5
        u = Q.pop(0)    # linha 6
        ordem.append(u) # linhas 7 e 8
        
        for v in G.arestas[u]:  # linha 9
            G.d_in[v] -= 1      # linha 10
            
            if G.d_in[v] == 0:  # linha 11
                Q.append(v)
                
    return ordem
        

########

g = Grafo()

g.adiciona_aresta("A", "B", 1)
g.adiciona_aresta("A", "C", 1)
g.adiciona_aresta("A", "F", 1)
g.adiciona_aresta("B", "E", 1)
g.adiciona_aresta("C", "E", 1)
g.adiciona_aresta("D", "F", 1)
g.adiciona_aresta("E", "D", 1)
g.adiciona_aresta("G", "D", 1)

ordem = khan(g)
print(ordem)