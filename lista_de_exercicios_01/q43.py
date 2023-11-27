materia1 = float(input("digite a nota da primeira matéria:"))
materia2 = float(input('digite a nota da segunda matéria:'))
materia3 = float(input("digite a nota da terceria matéria:"))
faltas = int(input('digite a quantidade de faltas totais:'))
media = (materia1 + materia2 +materia3) / 3
aulas_por_materias = 10
total_aulas = 3 * aulas_por_materias
frequencia = ((total_aulas - faltas) / total_aulas) * 100
aprovado = media >= 7 and frequencia >= 75
print('aluno aprovado', aprovado)