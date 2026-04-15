# Menu simples de pedidos

print("1 - Hambúrguer - R$ 10,00")
print("2 - Pizza - R$ 20,00")
print("3 - Refrigerante - R$ 8,00")

opção = input("Digite o número do item que deseja pedir: ")

if opção == "1":
    print("Você pediu um Hambúrguer.")
    print("Valor: R$ 10,00")
elif opção == "2":
    print("Você pediu uma Pizza.")
    print("Valor: R$ 20,00")
elif opção == "3":
    print("Você pediu um Refrigerante.")
    print("Valor: R$ 8,00")
else:
    print("Opção inválida.")
    
    # --- atividade encerrada ---