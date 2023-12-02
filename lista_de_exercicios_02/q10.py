#letra A
import random
#letra B
numero_secreto = random.randint(1, 100)
#letra C
palpite = 0
#letra D
while palpite != numero_secreto:
    palpite = int(input('Digite seu palpite (entre 1 e 100):'))
#letra E
    if  palpite > numero_secreto:
        print("tente um número menor.")
    elif palpite < numero_secreto:
        print("Digite um númmero maior.")
#letra F
print(f"Parabens! Você acertou o número secreto: {numero_secreto}")

