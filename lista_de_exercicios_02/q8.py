hora_inicial = int(input('Digite a hora inicial:'))
minuto_inicial = int(input('Digite o minuto inicial:'))
hora_final = int(input("Digite a hora final:"))
minuto_final = int(input('Digite o minuto final:'))

total = (hora_final * 60 + minuto_final) - (hora_inicial * 60 + minuto_inicial)

if 1 <= total <= 1440:
    duracao_horas = total // 60
    duracao_minutos = total // 60

    print (f'O jogo durou {duracao_horas} horas e {duracao_minutos} minutos')
else:
    print('duração inválida. O jogo deve ter no minimo 1 minuto e no maximo 24h')

#nao consegui fazer direito