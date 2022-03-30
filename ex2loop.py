quantidade_transacoes = int(input("Informe a quantidade de transações: "))
total_transacoes = 0
for n_trasacao in range(1, quantidade_transacoes + 1, 1):
    trasacao = float(input("Por favor informe a transação de numero {}. " .format(n_trasacao)))
    total_transacoes = total_transacoes + trasacao

media = total_transacoes /  quantidade_transacoes
print("Neste dia foi gasto um total de R$ {}, com uma media de R${:.2f} por transação." .format(total_transacoes, media))
