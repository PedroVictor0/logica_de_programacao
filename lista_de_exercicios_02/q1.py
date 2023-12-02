n1 = int(input("digite o primeiro número:"))
n2 = int(input('digite o segundo número:'))
n3 = int(input('digite o terceiro número:'))

if n1 > n2 and n1 > n3:
    print(f'O número maior é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O número maior é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O número maior é {n3}')

