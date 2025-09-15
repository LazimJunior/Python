import random
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_regressivo_1 = 10
contador_regressivo_2 = 11

primeiro_resultado = 0
segundo_resultado = 0

for digito_1 in nove_digitos:
    primeiro_resultado += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (primeiro_resultado * 10) % 11
digito_1 = digito_1  if digito_1 <= 9 else 0
print(digito_1)
digito_1 = str(digito_1)
dez_digitos = nove_digitos + digito_1

for digito_2 in dez_digitos:
    segundo_resultado += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (segundo_resultado * 10) % 11
digito_2 = digito_2  if digito_2 <= 9 else 0
print(digito_2)

cpf = dez_digitos + str(digito_2)

print(int(cpf))