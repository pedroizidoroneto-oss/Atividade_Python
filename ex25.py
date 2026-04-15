# Desconto no pedido

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade

if total > 50:
    desconto = total * 0.10
    total_com_desconto = total - desconto
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Total com desconto: R$ {total_com_desconto:.2f}")