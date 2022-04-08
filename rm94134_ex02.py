alunos = int(input("Quantos alunos existem na turma? "))
segunda = 0
terça = 0
quarta = 0
quinta = 0
sexta = 0
votacao = 0

while votacao < alunos:
    voto = input("Qual dia da semana você prefere: segunda, terça, quarta, quinta, sexta. ")
    if voto == "segunda":
        segunda = segunda + 1
    elif voto == "terça":
        terça = terça + 1
    elif voto == "quarta":
        quarta = quarta + 1
    elif voto == "quinta":
        quinta = quinta + 1
    elif voto == "sexta":
        sexta =  sexta + 1
    votacao = votacao + 1
        
print("Segunda teve ", segunda, "votos.")
print("terça teve ", terça, "votos.")
print("quarta teve ", quarta, "votos.")
print("qauinta teve ", quinta, "votos.")
print("sexta teve ", sexta, "votos.")