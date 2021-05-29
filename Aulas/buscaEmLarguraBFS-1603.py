def BFS(G,s):
   visitados = [s]
   distancias = {}
   distancias[s] = 0

   fila = [s]

   while len(fila) > 0:
      u = fila.pop(0)
      for v in G[u]:
         
         if v not in visitados:
            visitados.append(v)
            distancias[v] = distancias[u] + 1
            fila.append(v)
   return visitados, distancias

G = {
  'A' : ['B','C','D'],
  'B' : ['A', 'E'],
  'C' : ['A', 'D', 'E'],
  'D' : ['A','C','F'],
  'E' : ['B', 'F', 'C'],
  'F' : ['E', 'D']
}

visitados, distancias, arvore = BFS(G, 'A')
print(visitados)
print(distancias)
