### mapa do maroto
### estrutura de dados 2

### utilize um mapa inicialmente, depois faça o código rodar em todos eles

""" Mapa 1
>....v
"""

mapa1 = {'h': 6, 'v': 1, 'info': '>....v'}

""" Mapa 2
>.....v
.......
v.....<
...*...
>......
"""

mapa2 = {'h': 7, 'v': 5, 'info': '>.....v.......v.....<...*...>......'}

""" Mapa 3
>.v.
....
*.v.
....
..^.
"""

mapa3 = {'h': 4, 'v': 5, 'info': '>.v.....*.v.......^.'}

""" Mapa 4
>.....v..v
>....*....
^.....<..^
"""

mapa4 = {'h': 10, 'v': 3, 'info': '>.....v..v>....*....^.....<..^'}


def reconhece_grafo(mapa):
    
    h, v, info = mapa['h'], mapa['v'], mapa['info']
    
    M = []
    V = {}
    
    # transforma info em matriz
    for linha in range(v):
        M.append([]) # M[] -> M[[]]
        for coluna in range(h):
            M[linha].append(info[linha*h + coluna])
            
    direcoes = {
        '>':(1,0),
        '<':(-1,0),
        '^':(0,-1),
        'v':(0,1),
        '.':(0,0),
        '*':(0,0)
    }
    
    linha, coluna = 0, 0
    
    simbolo = M[linha][coluna]
    ultimo_vertice = (linha, coluna)
    V[str(ultimo_vertice)] = []
    
    while simbolo != '*':
        
        # verifica se atingiu limite do mapa
        if coluna >= h or coluna < 0 or linha >= v or linha < 0:
            break
        
        simbolo = M[linha][coluna]

        if simbolo != '.':
            dir_coluna, dir_linha = direcoes[simbolo]
            
            vertice_atual = (linha, coluna)
            if ultimo_vertice != vertice_atual:
                
                # verifica se o vertice ja nao foi adicionado
                if str(vertice_atual) in V:
                    break

                V[str(ultimo_vertice)].append(vertice_atual)
                
            ultimo_vertice = vertice_atual
            V[str(ultimo_vertice)] = []
            
        linha += dir_linha
        coluna += dir_coluna
        
    return M, V


def navegacao(M,V):
    
    posicao = (0,0)
    linha, coluna = posicao
    simbolo = M[linha][coluna]
    
    while simbolo != '*':
        
        adjacencias = V[str(posicao)]
        
        if len(adjacencias) <= 0:
            break
        
        posicao = adjacencias.pop()
        linha, coluna = posicao
        simbolo = M[linha][coluna]
        
    return simbolo

#########################################

for mapa in [mapa1,mapa2,mapa3,mapa4]:

    M, V = reconhece_grafo(mapa)
    destino = navegacao(M, V)

    if destino == '*':
        for i in M:
            print(i)
