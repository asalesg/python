print("App da lição")
assinatura_cliente = input("insira o numero correspondente a assinatura: 1 - Básica,   2 - Silver, 3 - Gold  4 - Platium. ")
faturamento_anual = float(input("Insira o faturamento anual: "))
valor_pagamento = 0

if assinatura_cliente.upper() == "1":
        valor_pagamento = faturamento_anual * 0.3
elif assinatura_cliente.upper() == "2":
        valor_pagamento = faturamento_anual * 0.2
elif assinatura_cliente.upper() == "3":
        valor_pagamento = faturamento_anual * 0.1
elif assinatura_cliente.upper() == "4":
        valor_pagamento = faturamento_anual * 0.05
else:
    print("Categoria não reconhecida")
    
print("o valor a ser pago é {}" .format(valor_pagamento))