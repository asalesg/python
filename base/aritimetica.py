n1=int(input('Digite um valor: '))
n2=int(input('Digite outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2 #divisao inteira
e= n1**n2 #exponenciação n1 elevado a n2
print('A soma é {}, o produto é {}, e a divisão é {:.3f}' .format(s, m, d)) #formatação pra ficar 3 pontos flutuantes
print('Divisão inteira {} e \n potência {}' .format(di, e)) # \n quebra linha

#print('A soma vale {}' .format(n1+n2)) escreve assim pq não uso a variavel depois e não gasta memoria a toa. app desempenho top uahuah