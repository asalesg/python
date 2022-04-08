#esse programa calcula a velocidade media

print ("Esse é o calculador de velocidade media")
distancia = input("Digite a distancia percorrida: ")
tempo = input ("Digite o tempo percorrido: ")
velocidade_media = float (distancia) / float (tempo)
print("A velocidade media calculada foi de {:.2f} km/h" .format(velocidade_media))
#dentro das chaves eu formatei a resposta em colcoar 2 casas decimais no formato FLOAT