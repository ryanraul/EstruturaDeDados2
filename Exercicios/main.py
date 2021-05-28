# Em grupos de até 6 alunos, vocês deverão encontrar uma árvore geradora qualquer no mapa de Hoenn e uma árvore geradora mínima.
# Como ponto de partida, qualquer cidade do mapa pode ser considerada.

# Leve em conta que você está habilitada a trafegar nas rotas aéreas, aquáticas e terrestres.

# 190961 Gabriel Augusto Nogueira
# 190953 Raul Ryan Deaque Silva
# 190810 Vitor Joaquim de Carvalho Gois 
# 190702 Otavio Cordeiro de Freitas
# 190301 Elias Della Torre Costa
# 190468 Lucas Tonholi
# 190583 Gabriel José Ferraz Perin 

##########################################################################

# importando uma biblioteca que possui suporte para numeros infinitos
import math
import copy

class Grafo:
    
    def __init__(self):
        self.vertices = []
        self.arestas = {}
        self.pesos = {}

    def adiciona_vertice(self,valor):
        self.vertices.append(valor)
        self.arestas[valor] = []
    
    def adiciona_aresta(self,origem,destino,peso):
        
        if origem not in self.vertices:
            self.adiciona_vertice(origem)
        
        if destino not in self.vertices:
            self.adiciona_vertice(destino)
        
        # Adicionando as arestas do grafo nao direcionado
        self.arestas[origem].append(destino)
        self.arestas[destino].append(origem)

        # Adicionando o peso da aresta
        self.pesos[(origem,destino)] = peso
        self.pesos[(destino,origem)] = peso

def menor_distancia (T,distancias):
    vertice_menor_distancia = None
    menor_distancia = None

    for vertice in T:
        if menor_distancia is None or distancias[vertice] < menor_distancia:
            vertice_menor_distancia = vertice
            menor_distancia = distancias[vertice]

    return vertice_menor_distancia

def dijkstra (grafo, origem):
    
    dist = {}
    dist[origem] = 0
    T = []
    T.append(origem)
    P = []

    while len(T) > 0:
        
        v = menor_distancia(T,dist)
        
        T.pop(T.index(v))
        P.append(v)

        for u in grafo.arestas[v]:

            if u in T:
                dist[u] = min(dist[u], dist[v] + grafo.pesos[(u,v)])
            
            elif u not in P:
                dist[u] = dist[v] + grafo.pesos[(v,u)]
                T.append(u)
    return dist

def adiciona_rotas_aereas(grafo):
    grafo.adiciona_aresta('Petalburg','Verdanturf',7)
    grafo.adiciona_aresta('Dewford','Littleroot',5)
    grafo.adiciona_aresta('Dewford','Pacifidlog',16)
    grafo.adiciona_aresta('Pacifidlog','Mauville',12)
    grafo.adiciona_aresta('Pacifidlog','Fortree',14)
    grafo.adiciona_aresta('Pacifidlog','Mossdeep',14)
    grafo.adiciona_aresta('Mauville','Lavaridge',6)
    grafo.adiciona_aresta('Mauville','Lilycove',14)

    return grafo

def adiciona_rotas_aquaticas(grafo):
    grafo.adiciona_aresta('Petalburg','Dewford',9)
    grafo.adiciona_aresta('Dewford','Slateport',20)
    grafo.adiciona_aresta('Slateport','Pacifidlog',11)
    grafo.adiciona_aresta('Pacifidlog','Ever Grand',15)
    grafo.adiciona_aresta('Pacifidlog','Sootopolis',17)
    grafo.adiciona_aresta('Ever Grand','Lilycove',13)
    grafo.adiciona_aresta('Sootopolis','Mossdeep',8)
    grafo.adiciona_aresta('Sootopolis','Lilycove',6)
    grafo.adiciona_aresta('Lilycove','Mossdeep',6)

    return grafo

def adiciona_rotas_terrestes(grafo):
    grafo.adiciona_aresta('Petalburg','Oldale',2)
    grafo.adiciona_aresta('Petalburg','Rustboro',6)
    grafo.adiciona_aresta('Oldale','Littleroot',5)
    grafo.adiciona_aresta('Rustboro','Verdanturf',4)
    grafo.adiciona_aresta('Rustboro','Fallarbor',9)
    grafo.adiciona_aresta('Verdanturf','Mauville',2)
    grafo.adiciona_aresta('Fallarbor','Mauville',19)
    grafo.adiciona_aresta('Mauville','Slateport',8)
    grafo.adiciona_aresta('Mauville','Fortree',9)
    grafo.adiciona_aresta('Fortree','Lilycove',7)

    return grafo

# Algoritmo de busca em largura modificado para encontrar uma arvore geradora
def BFS(grafo,s):
    lista = []
    visitados = []
    caminhos = []
    
    lista.append(s)
    visitados.append(s)

    while len(lista) > 0:
        u = lista.pop(0)
        for v in grafo.arestas[u]:
            if v not in visitados:
                visitados.append(v)
                lista.append(v)
                caminhos.append((u,v))
    return caminhos

# Algoritmo para criar uma arvore geradora minima atraves de um grafo
def PRIM(grafo,s):
    
    distancias = dict()

    # Varrendo todos os vertices e definindo uma distancia Infinita para cada um deles
    for v in grafo.vertices:
        distancias[v] = math.inf
    
    # Define a distancia da origem como sendo zero (ponto de partida)
    distancias[s] = 0

    # Criacao do dicionario de arestas
    arestas_escolhidas = dict()
    arestas_escolhidas[s] = (s,s)

    # Criacao de um dicionario temporario que possui todos os vertices do problema
    TEMP = copy.deepcopy(grafo.vertices)
    
    # Criacao de um dicionario que possui os caminhos da arvore geradora minima
    caminhos = []

    while len(TEMP) > 0:
        
        # Vertice utilizado na iteracao
        v = None

        # Escolhendo vertice de distancia minima
        for u in TEMP:
            if(v is None or distancias[u] < distancias[v]):
                v = u
        
        TEMP.remove(v)

        #Verificando se nao eh o caminho inicial, exemplo: (s,s)
        if v is not s:
            # Adiciona a aresta com menor distancia escolhida
            caminhos.append(arestas_escolhidas[v])

        for u in grafo.arestas[v]:
            if u in TEMP and distancias[u] > grafo.pesos[(v,u)]:
                distancias[u] = grafo.pesos[(v,u)]
                arestas_escolhidas[u] = (v,u)

    return caminhos

def calcula_distancia_caminho(grafo,caminhos):
    total = 0
    for caminho in caminhos:
        total = total + grafo.pesos[caminho]
    
    return total
#####################################################################

g = Grafo()

# Adicionando os vertices e arestas no grafo
g = adiciona_rotas_terrestes(g)
g = adiciona_rotas_aquaticas(g)
g = adiciona_rotas_aereas(g)

# Montando a arvore geradora qualquer
arvore_geradora_qualquer = BFS(g,'Petalburg')
distancia_arvore_geradora_qualquer = calcula_distancia_caminho(g,arvore_geradora_qualquer)

print()
print(arvore_geradora_qualquer)
print(f'O total percorrido pelo caminho foi: {distancia_arvore_geradora_qualquer}')

# Montando a arvore geradora minima
arvore_geradora_minima = PRIM(g,'Petalburg')
distancia_arvore_geradora_minima = calcula_distancia_caminho(g,arvore_geradora_minima)

print()
print(arvore_geradora_minima)
print(f'O total percorrido pelo caminho foi: {distancia_arvore_geradora_minima}')


####################### EXEMPLO DO GRAFO FEITO EM AULA  ##############################################

# g1 = Grafo()
# g1.adiciona_aresta('A','B',3)
# g1.adiciona_aresta('A','C',5)
# g1.adiciona_aresta('A','D',1)
# g1.adiciona_aresta('B','E',4)
# g1.adiciona_aresta('C','E',8)
# g1.adiciona_aresta('C','D',4)
# g1.adiciona_aresta('D','F',3)
# g1.adiciona_aresta('E','F',7)

# arvore_geradora_qualquer = BFS(g1,'C')
# dist_arvore_qualquer = calcula_distancia_caminho(g1,arvore_geradora_qualquer)

# arvore_geradora_minima = PRIM(g1,'C')
# dist_arvore_minima = calcula_distancia_caminho(g1,arvore_geradora_minima)

# print()
# print(arvore_geradora_qualquer)
# print(dist_arvore_qualquer)

# print()
# print(arvore_geradora_minima)
# print(dist_arvore_minima)




