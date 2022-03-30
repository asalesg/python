valor_bruto = float(input("Por favor, informe o valor bruto da viagem: "))
categoria = input("Por favor, informe a categoria: ECONÔMICA, EXECUTIVA ou PRIMEIRA CLASSE: ")
quantidade_viajante = int(input("Por favor, informe a quantidade de viajantes: "))
valor_desconto = 0
if categoria.upper() == "ECONÔMICA":
    if quantidade_viajante == 2:
        valor_desconto = valor_bruto * 0.03
    elif quantidade_viajante == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidade_viajante >= 4:
        valor_desconto = valor_bruto * 0.05
    else:
        print("O que eu faço agora? Se p valor for 1 eu não sei o que tenho que fazer :(")
elif categoria.upper() == "EXECUTIVA":
    if quantidade_viajante == 2:
        valor_desconto = valor_bruto * 0.05
    elif quantidade_viajante == 3:
        valor_desconto = valor_bruto * 0.07
    elif quantidade_viajante >= 4:
        valor_desconto = valor_bruto * 0.08
    else:
        print("Aqui também pode ser que o valor seja 1 e eu não sei como seguir! :((((")
elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajante == 2:
        valor_desconto = valor_bruto * 0.1
    elif quantidade_viajante == 3:
        valor_desconto = valor_bruto * 0.15
    elif quantidade_viajante >= 4:
        valor_desconto = valor_bruto * 0.2
    else:
        print("Olha eu perdido de novo aqui. Sou um código que não tem sei o que fazer nesta condição de else")
else:
    print("Categoria inexistente, não será concedido nenhum desconto")
    valor_liquido = valor_bruto - valor_desconto