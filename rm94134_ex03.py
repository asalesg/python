total_alunos = 50
media_par = 0
media_impar = 0
for impar in range (1, total_alunos, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES" )
    soma_impar = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: "  .format(impar)))
    
for par in range (2, total_alunos + 2, 2):
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    soma_par = int(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: "  .format(par)))
    
media_par = media_par + soma_par / 25
media_impar = media_impar + soma_impar / 25

print("A média da parte par foi: {} " .format(media_par))
print("A média da parte impar foi: {} " .format(media_impar))

if media_par > media_impar:
    print("A parte par teve média maior.")
else:
    print("A parte impar teve média maior.")