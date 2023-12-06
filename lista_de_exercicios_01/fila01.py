def exibir_fila(fila):
    print("Fila:", fila)
    print("Tamanho da fila:", len(fila))

fila = list(range(1, 11))  
while True:
    print("F - Adicionar alguém ao fim da fila")
    print("A - Atender uma pessoa (remover do início da fila)")
    print("S - Sair do sistema")

    opcao = input("Digite a operação desejada (F, A ou S): ").upper()

    if opcao == 'F':
        fila.append(len(fila) + 1)
        exibir_fila(fila)
    elif opcao == 'A':
        if fila:
            atendido = fila.pop(0)
            print(f"Atendendo a pessoa com ticket {atendido}")
            exibir_fila(fila)
        else:
            print("A fila está vazia.")
    elif opcao == 'S':
        print("Saindo do sistema.")
        break
    else:
        print("Operação inválida. Tente novamente.")

