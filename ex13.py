Sistema de nota

nota = float(input("Digite a nota do aluno: "))

if nota >= 18:
    print("O aluno foi aprovado.")
elif nota >= 8 and nota < 17:
    print("O aluno está em recuperação.")
else:
    print("O aluno foi reprovado.")
