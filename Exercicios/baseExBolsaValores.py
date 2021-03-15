acoes = 0
carteira = 100
FACN = [8.50, 8.0, 9.0, 8.5, 8.5, 9.0, 8.0, 7.0]

## única regra: não acessar índice futuro à posição atual

for valor in FACN:
    # código para fazer compra
    if carteira > valor:
        qtde_compra = carteira // valor
        acoes += qtde_compra
        carteira -= qtde_compra * valor
        
    # código para fazer venda
    qtde_venda = 1
    if qtde_venda <= acoes:
        acoes -= qtde_venda
        carteira += qtde_venda * valor
        
# código para mostrar o resultado da carteira
carteira += acoes * valor
print("Carteira: R$", carteira)
