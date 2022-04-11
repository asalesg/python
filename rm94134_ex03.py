total_alunos = 50
soma_impar = 0
soma_par = 0
for impar in range (1, total_alunos, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES" )
    soma_impar += float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: "  .format(impar)))
    
    
for par in range (2, total_alunos + 2, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    soma_par += float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: "  .format(par)))
    
print("A média da parte par foi: {} " .format(soma_par/25))
print("A média da parte impar foi: {} " .format(soma_impar/25))

if soma_par > soma_impar:
    print("A parte par teve média maior.")
else:
    print("A parte impar teve média maior.")