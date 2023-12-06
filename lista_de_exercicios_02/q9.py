


import random

opcao_computador = random.randint(0 ,2)



match opcao_computador:
    case 0:
        opcao_computador = 'pedra'
    case 1:
        opcao_computador = 'papel'
    case 2:
        opcao_computador = 'tesoura'

opcao_jogador = input('Qual opção você deseja jogar(Pedra, Papel ou Tesoura)')


if (opcao_jogador  == 'pedra' and opcao_computador == 'tesoura') or \
(opcao_jogador == 'papel' and opcao_computador == 'pedra') or \
(opcao_jogador == 'tesoura' and opcao_computador == 'papel'):
    print( 'Jogador venceu!')
else:
    print( 'Computador venceu')

if opcao_jogador == opcao_computador:
    print('empate')