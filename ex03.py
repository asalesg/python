voto1 = input("informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")
voto2 = input("informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")
voto3 = input("informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")
voto4 = input("informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")
voto5 = input("informe qual premio deseja ganhar: PLAYSTATION, XBOX ou NINTENDO ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto1.upper() == "XBOX":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 1 digitou um console inexistente e seu voto sera desconsiderado")

print("Playstation: {}\nXbox: {}\nNintendo: {}" .format(playstation, xbox, nintendo))

if voto2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto2.upper() == "XBOX":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 2 digitou um console inexistente e seu voto sera desconsiderado")

print("Playstation: {}\nXbox: {}\nNintendo: {}" .format(playstation, xbox, nintendo))

if voto3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto3.upper() == "XBOX":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 3 digitou um console inexistente e seu voto sera desconsiderado")

print("Playstation: {}\nXbox: {}\nNintendo: {}" .format(playstation, xbox, nintendo))

if voto4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto4.upper() == "XBOX":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 4 digitou um console inexistente e seu voto sera desconsiderado")

print("Playstation: {}\nXbox: {}\nNintendo: {}" .format(playstation, xbox, nintendo))

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O Colaborador 5 digitou um console inexistente e seu voto sera desconsiderado")

print("Playstation: {}\nXbox: {}\nNintendo: {}" .format(playstation, xbox, nintendo))

if playstation > xbox and playstation > nintendo:
    print ("O Console escolhido foi playstation") #ou usar dois if (um dentro do outro)
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi o Xbox")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi o Nintendo ")
else:
    print("Houve empate, favor entrar em contato com a direção")