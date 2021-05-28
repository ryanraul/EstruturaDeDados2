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
            if v not in visitados and self.pesos[(u,v)] > 0:
               fila.append(v)
               visitados.append(v)
               caminho[v] = u

      return True if t in visitados else False

   def ford_fulkerson(self, origem, destino):

      fluxo_max = 0
      caminho = {}
         
      while self.BFS(origem, destino, caminho):
         caminho_fluxo = float("Inf")

         s = destino
         while(s != origem):
            caminho_fluxo = min(caminho_fluxo, self.pesos[(caminho[s], s)])
            s = caminho[s]

         fluxo_max += caminho_fluxo

         v = destino
         while(v != origem):
            u = caminho[v]
            self.pesos[(u,v)] -= caminho_fluxo
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

print(g.arestas)
print(g.vertices)
print(g.pesos)
print("Fluxo maximo: ", g.ford_fulkerson("s", "t"))
