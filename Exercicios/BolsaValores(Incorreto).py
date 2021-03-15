acoes = 0
carteira = 100
FACN = [8.50, 8.0, 9.0, 8.5, 8.5, 9.0, 8.0, 7.0]
valores_anteriores = []
determinantes = {
   'compra': 0,
   'vender': 0
}

## única regra: não acessar índice futuro à posição atual

for valor in FACN:
   valores_anteriores.append(valor)

   for valor_aterior in valores_anteriores:
      if valor_aterior > valor:
         determinantes['compra'] = 0
         determinantes['vender'] = determinantes['vender'] + 1
      
      if valor_aterior < valor:
         determinantes['vender'] = 0
         determinantes['compra'] = determinantes['compra'] + 1

   print(determinantes)
   # código para fazer compra
   if valor_aterior > valor and determinantes['vender'] <= 3:
      qtde_compra = carteira // valor
      acoes += qtde_compra
      carteira -= qtde_compra * valor
   
   if valor_aterior < valor and determinantes['compra'] <= 3 :
      qtde_venda = acoes // 2
      acoes -= qtde_venda
      carteira += qtde_venda * valor

   # # código para fazer venda
   # qtde_venda = 1
   # if qtde_venda <= acoes:
   #    acoes -= qtde_venda
   #    carteira += qtde_venda * valor

   # código para mostrar o resultado da carteira
   carteira += acoes * valor
   print("Carteira: R$", carteira)