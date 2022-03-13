nome=input("digite seu nome: ")
idade=int(input("digite a idade "))
if idade>=65:
    print("o paciente " + nome + " POSSUI atendimento prioritario")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário")