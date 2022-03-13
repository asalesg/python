nome=input("Digite o nome: ")
idade=int(input("DIgite uma idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?") .upper()
if idade>=65:
    print("O paciente " + nome + " POSSUI atendimento prioritario")
elif doenca_infectocontagiosa=="sim":
    print("O paciente " + nome + " deve ser direcionado para a sala reservada. ")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritario e pode aguardar na sala comum.")