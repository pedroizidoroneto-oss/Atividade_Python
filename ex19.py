# Prioridade
idade = int(input("Digite a idade: "))
gestante = input("Está gestante? (s/n): ")

if idade >= 60 or gestante == "s":
    print("Senha preferencial.")
else:
    print("Atendimento normal.")