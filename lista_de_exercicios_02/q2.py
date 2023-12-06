salario = float(input('digite o valor do seu salário:'))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento
print(f'O aumento do salário foi de R${aumento}')
print(f'O novo salario é R${novo_salario}')
