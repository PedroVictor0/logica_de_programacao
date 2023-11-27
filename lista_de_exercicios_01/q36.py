#Prodessora não estava entendendo, então perguntei pro chatgpt como fazia para não ficar sem entender a questão
valor = int(input("digite um valor:"))
notas100 = notas50 = notas20 = notas10 = nota5 = nota2= nota1= 0
while valor != 0:
    if valor >=100:
        notas100 += 1
        valor -=100
    elif valor >=50:
        notas50 += 1
        valor -=50
    elif valor >=20:
        notas20 += 1
        valor -=20
    elif valor >=10:
        notas10 += 1
        valor -=10
    elif valor >=5:
        nota5 += 1
        valor -=5
    elif valor >=2:
        nota2 += 1
        valor -=2
    elif valor >=1:
        nota1 += 1
        valor -=1
    else:
        nota1 += 1
        valor -= 1
print("valor lido:", valor)
print("notas de 100:", notas100)
print("notas de 50:", notas50)
print("notas de 20:", notas20)
print("notas de 10:", notas10)
print("notas de 5", nota5)
print("notas de 2:", nota2)
print("notas de 1:", nota1)