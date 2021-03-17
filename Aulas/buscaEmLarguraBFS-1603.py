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

# Testes/Rascunhos
# def menor_caminho(distancias, inicio, fim):
#    i = 0
#    menor = [fim]
#    aux = 10
#    while i < distancias[fim]:
#       aux = 10
#       for adjacente in G[fim]:
#          if adjacente == inicio:
#             menor.append(adjacente)
#             break
#          if distancias[adjacente] < aux:
#             aux = distancias[adjacente]
#             adj_certo = adjacente
#       menor.append(adj_certo)
#       fim = adj_certo
#       i+=1
#    menor.append(inicio)
#    return menor

      


G = {
  'A' : ['B','C','D'],
  'B' : ['A', 'E'],
  'C' : ['A','G'],
  'D' : ['A','H'],
  'E' : ['B'],
  'F' : [],
  'G' : ['C','H'],
  'H' : ['D','G','I'],
  'I' : ['H']
}

visitados, distancias = BFS(G, 'A')
#menorCaminho = menor_caminho(distancias, 'E', 'I')
#print(menorCaminho)

print(visitados)
print(distancias)


