"""
| --- Implementação do algoritmo de Ford-Fulkerson --- |
| --------------- Integrantes do grupo --------------- |
|                                                      |
| + Nome: Elias Della Torre Costa - RA: 190301         |   
| + Nome: Gabriel José Ferraz Perin - RA: 190583       |   
| + Nome: Lucas Tonholi - RA: 190468                   |   
| + Nome: Otavio Cordeiro de Freitas - RA: 190702      |   
| + Nome: Raul Ryan Deaque Silva - RA: 190953          |
| + Nome: Vitor Joaquim de Carvalho Gois - RA: 190583  |
|                                                      |
| ---------------------------------------------------- |
"""
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
      self.pesos[(origem,destino)] = peso

   def BFS(self, s, t, caminho):

      visitados = [s]
      fila = [s]

      while len(fila) > 0:
         u = fila.pop(0)
    
         for v in self.arestas[u]:
            # O caminho apenas será composto por vertices cuja a aresta tenha o peso maior que zero
            if v not in visitados and self.pesos[(u,v)] > 0:
               fila.append(v)
               visitados.append(v)
               # Adiciona ao caminho do vertice (v) o vertice que tenha a ligação com o mesmo
               caminho[v] = u

      # Caso a rota até o destino ainda seja possivel retornar verdadeiro (True)
      return True if t in visitados else False

   def ford_fulkerson(self, origem, destino):

      fluxo_max = 0
      caminho = {}

      # Enquanto o destino estiver entre os vertices visitados, executa o processo.
      while self.BFS(origem, destino, caminho):
         caminho_fluxo = float("Inf")

         s = destino
         while(s != origem):
            # Recupera aresta com menor valor presente no caminho entre 'origem' e 'destino'
            caminho_fluxo = min(caminho_fluxo, self.pesos[(caminho[s], s)])
            s = caminho[s]
         
         # Incrementando o 'fluxo_max' com a aresta de menor valor inclusa no caminho entre a 'origem' e o 'destino'
         fluxo_max += caminho_fluxo

         v = destino
         while(v != origem):
            # Recuperando o vertice (u) que esta conectado ao vertice de destino (v)
            u = caminho[v]
            # Decrementando os valores das arestas que liga 'u' e 'v' com o menor valor entre as arestas do caminho (caminho_fluxo)
            self.pesos[(u,v)] -= caminho_fluxo
            # Alterando o vertice destino (v) para que ocorra a decrementação de todas arestas que compoe este caminho
            v = caminho[v]

      return fluxo_max


g = Grafo()

# -- Grafo exemplo (Aula 26/05) --

g.adiciona_aresta("s", "a", 15)
g.adiciona_aresta("s", "b", 4)
g.adiciona_aresta("a", "c", 12)
g.adiciona_aresta("c", "b", 3)
g.adiciona_aresta("c", "t", 7)
g.adiciona_aresta("b", "d", 10)
g.adiciona_aresta("d", "a", 5)
g.adiciona_aresta("d", "t", 10)

# -- Grafo exemplo --
# g.adiciona_aresta("s", "a", 13)
# g.adiciona_aresta("s", "b", 10)
# g.adiciona_aresta("s", "c", 10)
# g.adiciona_aresta("a", "d", 24)
# g.adiciona_aresta("b", "a", 5)
# g.adiciona_aresta("b", "f", 7)
# g.adiciona_aresta("b", "c", 15)
# g.adiciona_aresta("c", "f", 15)
# g.adiciona_aresta("d", "e", 1)
# g.adiciona_aresta("d", "t", 9)
# g.adiciona_aresta("e", "t", 13)
# g.adiciona_aresta("e", "f", 6)
# g.adiciona_aresta("f", "t", 16)

# print(g.arestas)
# print(g.vertices)
# print(g.pesos)
print("Fluxo maximo: ", g.ford_fulkerson("s", "t"))
