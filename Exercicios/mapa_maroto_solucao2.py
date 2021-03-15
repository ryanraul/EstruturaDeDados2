### mapa do maroto
### estrutura de dados 2
### utilize um mapa inicialmente, depois faça o código rodar em todos eles

mapa1 = {'h': 6, 'v': 1, 'info': '>....v'}
""" Mapa 1
>....v
"""

mapa2 = {'h': 7, 'v': 5, 'info': '>.....v.......v.....<...*...>......'}
""" Mapa 2
>.....v
.......
v.....<
...*...
>......
"""

mapa3 = {'h': 4, 'v': 5, 'info': '>.v.....*.v.......^.'}
""" Mapa 3
>.v.
....
*.v.
....
..^.
"""

mapa4 = {'h': 10, 'v': 3, 'info': '>.....v..v>....*....^.....<..^'}
""" Mapa 4
>.....v..v
>....*....
^.....<..^
"""

def CriaMatriz(mapa):
   global lista_adjacente
   col = 0
   matriz = []
   for g in range (mapa['v']):
      matriz.append([])
      for j in range(mapa['h']):
         if(mapa['info'][col] != '.'):
            lista_adjacente.append([])
         matriz[g].append(mapa['info'][col])
         col += 1
   return matriz

def PreencheVerticesListaAdjacente(matriz):
   global lista_adjacente, vertices
   l_pos = 0
   for i in range(len(matriz)):
      for j in range(len(matriz[i])):
         if matriz[i][j] != '.':
            vertices.append(matriz[i][j])
            if matriz[i][j] == '>':
               for y in range(j,len(matriz[i])):
                  if matriz[i][y] != '.' and y != j:
                     if matriz[i][y] != '<':
                        lista_adjacente[l_pos].append(matriz[i][y])
                     break
            if matriz[i][j] == 'v':
               for y in range(i, len(matriz)):
                  if matriz[y][j] != '.' and y != i:
                     if matriz[y][j] != '^':
                        lista_adjacente[l_pos].append(matriz[y][j])                  
                     break
            if matriz[i][j] == '<':
               for y in range(j, -1, -1):
                  if matriz[i][y] != '.' and y != j:
                     if matriz[i][y] != '>':
                        lista_adjacente[l_pos].append(matriz[i][y])
                     break
            if matriz[i][j] == '^':
               for y in range(i, -1, -1):
                  if matriz[y][j] != '.' and y != i:
                     if matriz[y][j] != 'v':
                        lista_adjacente[l_pos].append(matriz[y][j])
                     break
            l_pos += 1

def ConstroiCaminhoMapa():
   global vertices, lista_adjacente
   aux = vertices[0]
   pos_remove = 0
   for i in range(len(vertices)):
      if len(lista_adjacente[vertices.index(aux)]) > 0:
         caminho.append(lista_adjacente[vertices.index(aux)][0])
         pos_remove = vertices.index(aux)
         aux = lista_adjacente[vertices.index(aux)][0]
         vertices[pos_remove] = '.'

   return caminho

vertices = []
lista_adjacente = []
caminho = [] 

def VerificaMapa(mapa, nomeMapa):
   global lista_adjacente, vertices
   matriz = CriaMatriz(mapa)
   PreencheVerticesListaAdjacente(matriz)
   caminho = ConstroiCaminhoMapa()
   print("\nCaminho {0}: {1}".format(nomeMapa, caminho))
   # print("\nVertices: ", vertices)
   # print("\nTerminações: ", lista_adjacente)
   if caminho.count('*') != 0:
      print('\n' + nomeMapa + ' é verdadeiro!')

   lista_adjacente.clear()
   vertices.clear()
   caminho.clear()

VerificaMapa(mapa1, "Mapa 1")
VerificaMapa(mapa2, "Mapa 2")
VerificaMapa(mapa3, "Mapa 3")
VerificaMapa(mapa4, "Mapa 4")

# DICAS:
#
# (1) pense como ler os dados do mapa e transformar em um grafo, (os mapas são dicionários) 
#     cada direção é um vértice e aponta com qual vértice seguinte se conecta
#
# (2) as arestas não devem ser utilizadas duas vezes para eles não se perderem no castelo
#
# (3) utilize papel e caneta para verificar se as informações de vértices e arestas estão corretas
#     a medida que você implementar
#
# (4) ao final, basta imprimir qual é o mapa CORRETO, para todos os outros apenas ignore

