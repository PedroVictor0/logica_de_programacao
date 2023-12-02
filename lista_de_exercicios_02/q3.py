consumo = float(input('Digite a quantidade de kWh consumidos: '))
instalacao = input('Digite o tipo de instalação (R para residências, I para indústrias, C para comércios)')

if instalacao == 'R':
    if consumo <= 500:
        preco = consumo * 0.40
    else:
        preco = consumo * 0.65
elif instalacao == 'I':
    if consumo <= 1000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
elif instalacao == 'C': 
        preco = consumo * 0.55
else:
     preco = consumo * 0.60

if preco > 0:
     print(f"O preço a pagar é: R${preco}")
else:
     print(f'Tipo de instalação inválido')
     
    



