n = int(input('Digite um numero dos minutos atuais: '))

c = 0
f = 1
for c in range (1, n):
    f *= n
    n -= 1
print('Sua senha é: LIBERDADE{}'.format(f))