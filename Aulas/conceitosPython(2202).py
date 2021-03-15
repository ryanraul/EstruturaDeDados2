alunos = ["Raul", "Ryan", "Deaque", 0 , True]
#print(alunos)

matriz = [[1,2],[3,4]]
#print(matriz[0][1])

lista = []
lista.append(1)      #Adiciona valor na posicao final da lista
lista.insert(0, 2)   #Adiciona o valor 2 na posicao inicial(push)
lista.append(3)      #Adiciona valor na posicao final da lista
lista.pop()          #Retira o ultimo valor da lista
lista.remove(1)      #Retira o valor "1" da lista
#print(lista)

lista2 = ["Raul","Ryan",3,4,'Raul']
#print(lista2.count('Raul'))

for elemento in lista2:
   pass
   #print(elemento)

for i, elemento in enumerate(lista2):
   if i == 2:
      break
   #print(i, elemento)

for x in range(5):
   pass
   #print(x)

for x in range(len(lista2)):
   pass
   #print(x)

cont = 0
while cont < 3:
   #print(lista2[cont])
   cont+=1


