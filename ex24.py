#Total do pedido

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade

print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Total: R$ {total:.2f}")