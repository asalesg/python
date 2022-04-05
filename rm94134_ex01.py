"""1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

 

Nível

Porcentagem sobre o faturamento

Basic

30%

Silver

20%

Gold

10%

Platinum

5%"""

print("App da lição")
assinatura_cliente = input("insira o tipo de assinatura: Básica, Silver, Gold ou Platium. ")
faturamento_anual = float(input("Insira o faturamento anual: "))
valor_pagamento = 0

if assinatura_cliente.upper() == "Básica":
    if quantidade_viajante == 2:
        valor_desconto = faturamento_anual * 0.3
    elif quantidade_viajante == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidade_viajante >= 4:
        valor_desconto = valor_bruto * 0.05
    else: