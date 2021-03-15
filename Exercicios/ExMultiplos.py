nums = input().split()

A, B = nums

A = int(A)
B = int(B)

maiorAB = (A + B + abs(A - B)) / 2

if(A > B and A % B == 0):
   print("Sao Multiplos")
elif(B % A == 0):
   print("Sao Multiplos")
else:
   print("Nao sao Multiplos")


