notas = []

opcao = -1

while opcao !=4:
    print("1 - Informar notas \n 2 - Exibir notas \n 3 - calcular média \n 4- Sair")
    opcao = int(input("Escolha sua opção: "))
    if opcao == 1:
        notas.append(float(input("Digite a nota: ")))
    elif opcao == 2:
        for x in notas:
            print(x)
    elif opcao == 3:
        print(sum(notas)/len(notas))