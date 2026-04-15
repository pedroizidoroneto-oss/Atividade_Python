# Aprovação alternativa

nota = float(input("Digite a nota do aluno: "))
frequencia = float(input("Digite a frequência do aluno (em %): "))

if nota >= 7 or frequencia >= 90:
    print("situação especial de aprovação!")
else:
    print("Aluno em avaliação.")