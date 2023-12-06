valor = float(input("digite o valor"))
valor_em_centavos = int(valor * 100)
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = 0
moedas1 = moedas050 = moedas025 = moedas010 = moedas005 = moedas001 = 0
while valor_em_centavos != 0:
    if valor_em_centavos >=10000:
        notas100 += 1
        valor_em_centavos -=1000
    elif valor_em_centavos >=5000:
        notas50 += 1
        valor_em_centavos -=5000
    elif valor_em_centavos >=2000:
        notas20 += 1
        valor_em_centavos -=2000
    elif valor_em_centavos >=1000:
        notas10 += 1
        valor_em_centavos -=1000
    elif valor_em_centavos >=500:
        notas5 += 1
        valor_em_centavos -=500
    elif valor_em_centavos >=200:
        notas2 += 1
        valor_em_centavos-=200
    elif valor_em_centavos >=100:
        moedas1 += 1
        valor_em_centavos -=100
    elif valor_em_centavos >= 50:
        moedas050 += 1
        valor_em_centavos -=50
    elif valor_em_centavos >=25:
        moedas025 += 1
        valor_em_centavos -= 25
    elif valor_em_centavos >= 10:
        moedas010 += 1
        valor_em_centavos -= 10
    elif valor_em_centavos >= 5:
        moedas005 += 1
        valor_em_centavos -= 5
    else:
        moedas001 +=1
        valor_em_centavos -= 1
        
print("notas de 100:", notas100)
print("notas de 50:", notas50)
print("notas de 20:", notas20)
print("notas de 10:", notas10)
print("notas de 5", notas5)
print("notas de 2:", notas2)
print("notas de 1:", moedas1)
print("notas de 0,50", moedas050)
print("notas de 0,25", moedas025)
print("notas de 0,10", moedas010)
print("notas de 0,05", moedas005)
print("moedas de 0,01", moedas001)

