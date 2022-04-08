print('--------Dias Da Semana--------')
print('Me diga quantos votos tiveram os dias da semana:')

dias = []
segunda = int(input('Segunda:'))
dias.append(segunda)
terca = int(input('terca:'))
dias.append(terca)
quarta = int(input('quarta:'))
dias.append(quarta)
quinta = int(input('quinta:'))
dias.append(quinta)
sexta = int(input('sexta:'))
dias.append(sexta)

dias.sort()
print(dias)

if dias[4]==segunda:
    print('O dia escolhido foi segunda')
elif dias[4]==terca:
    print('O dia escolhido foi terca')
elif dias[4]==quarta:
    print('O dia escolhido foi terca')
elif dias[4]==quinta:
    print('O dia escolhido foi quinta')
elif dias[4]==sexta:
    print('O dia escolhido foi: sexta', 'com ', dias[4], ' votos.')