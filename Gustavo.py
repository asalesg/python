nums = []
for c in range (0, 3):
  num = int(input("Digite os numeros : "))
  if len(num) < 1:
    print("Não pode ser vazio")
  else:
    nums.append(num)

nums.sort()
maior = nums(-1)
menor = nums(0)
print('maior: ' + maior + "| menor: " + menor)