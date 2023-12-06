pilha = list(range(1, 6)) 

while True:
    print("\nOpções:")
    print("E - Empilhar um novo prato")
    print("D - Desempilhar (remover um prato da pilha)")
    print("S - Sair do sistema")

    opcao = input("Digite a operação desejada (E, D ou S): ").upper()

    if opcao == 'E':
        pilha.append(len(pilha) + 1)
        print("Pilha:", pilha)
        print("Tamanho da pilha:", len(pilha))
    elif opcao == 'D':
        if pilha:
            desempilhado = pilha.pop()
            print(f"Desempilhando o prato {desempilhado}")
            print("Pilha:", pilha)
            print("Tamanho da pilha:", len(pilha))
        else:
            print("A pilha está vazia.")
    elif opcao == 'S':
        print("Saindo do sistema.")
        break
    else:
        print("Operação inválida. Tente novamente.")
