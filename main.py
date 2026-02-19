lista = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1 - Adicionar item")
    print("2 - Ver lista")
    print("3 - Remover item")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Adicionar item
        item = input("Qual item deseja adicionar? ")
        lista.append(item)
        print(f"Item '{item}' adicionado com sucesso")

    elif opcao == "2":
        # Ver lista
        if not lista:
            print("A lista está vazia")
        else:
            print("Lista de compras:")
            for i, item in enumerate(lista):
                print(f"{i + 1} - {item}")

    elif opcao == "3":
        # Remover item
        if not lista:
            print("A lista está vazia")
            continue  # volta para o menu se não houver itens

        # Mostrar lista numerada
        print("Lista de compras:")
        for i, item in enumerate(lista):
            print(f"{i + 1} - {item}")

        # Perguntar qual item remover
        escolha = input("Digite o número do item que deseja remover: ")

        # Validar se é um número
        if not escolha.isdigit():
            print("Número inválido")
            continue

        indice = int(escolha) - 1  # transformar número em índice

        # Validar se o índice está dentro do intervalo
        if indice < 0 or indice >= len(lista):
            print("Número inválido")
            continue

        # Remover o item
        removido = lista.pop(indice)
        print(f"Item '{removido}' removido com sucesso")

    elif opcao == "4":
        # Sair do programa
        print("Até mais!")
        break

    else:
        print("Opção inválida, tente novamente")