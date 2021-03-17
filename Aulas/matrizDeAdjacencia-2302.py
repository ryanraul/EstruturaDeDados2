#Representação de grafos

# matriz de adjacencia

#   q1 ------ q3
#   |
#   q2

V = ['Q1', 'Q2', 'Q3']
E = [('Q1','Q2'), ('Q1','Q3'), ('Q2','Q1'), ('Q3','Q1')]


M = []
for i in range(len(V)):
    M.append([0] * len(V))
    

for i, j in E:
    M[V.index(i)][V.index(j)] = 1
    
    
print(M)
