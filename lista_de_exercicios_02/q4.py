distancia = float(input('Qual é a distância você deseja percorrer em km?' ''))


if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f"O preço da passagem é R${preco}")

