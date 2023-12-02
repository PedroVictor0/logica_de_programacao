A = int(input('Digite seu primeiro valor:'))
B = int(input('Digite seu segundo valor:'))
C = int(input('Digite seu terceiro valor:'))
D = int(input('Digite seu quarto valor:'))

if (B > C) and (D > A) and (C + D > A + B) and (C and D > 0) and (A % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores não aceitos')