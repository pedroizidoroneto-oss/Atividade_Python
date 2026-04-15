# Condição com AND

idade = int(input("Digite a idade: "))
carteira = input("Tem carteira? (s/n): ")

if idade >= 18 and carteira == "s":
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")
    