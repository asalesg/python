print("Verificador de frequências cardíacas")
idade = int(input("Por favor, informe sua idade"))
bpm = int(input("Por favor, informe seus batimentos"))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Frequencia cardiaca adequada")
    else: 
        print("Freqiencia cardiaca inadequada")
elif idade >=8 and idade < 17:
    if bpm >= 80 and bpm <= 100:
        print("Frequencia cardiaca adequada")
    else: 
        print("Freqiencia cardiaca inadequada")
elif idade >=18 and idade < 60:
    if bpm >= 70 and bpm <= 80:
        print("Frequencia cardiaca adequada")
    else: 
        print("Freqiencia cardiaca inadequada")
elif idade >=60:
    if bpm >= 50 and bpm <= 60:
        print("Frequencia cardiaca adequada")
    else: 
        print("Freqiencia cardiaca inadequada")
else:
    print("Não existem dados para a idaed indicada")