from importlib import import_module


n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > n2:
    print("O maior dos numeros é ", n1)
elif n2 > n1:
    print("O maior dos numeros é ",  n2 )
else:
  print("Os numeros são iguais")