# lista de adjacencia

#   q1 ------ q3
#   |
#   q2

V = ['Q1', 'Q2', 'Q3']
E = [('Q1','Q2'), ('Q1','Q3'), ('Q2','Q1'), ('Q3','Q1')]

L = []
for i in range(len(V)):
    L.append([])

for i, j in E:
    L[V.index(i)].append(j)

print(L)
