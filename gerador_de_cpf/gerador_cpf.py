import random

for _ in range(15):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo1 = 10

    resultado_digito1 = 0
    for digito in nove_digitos:
        resultado_digito1 = resultado_digito1 + int(digito) * contador_regressivo1
        contador_regressivo1 -= 1
    digito1 = (resultado_digito1 * 10) % 11

    digito1 = digito1 if digito1 <= 9 else 0


    dez_digitos = nove_digitos + str(digito1)
    contador_regressivo = 11

    resultado_digito2 = 0
    for digito in dez_digitos:
        resultado_digito2 = resultado_digito2 + (int(digito) * contador_regressivo)
        contador_regressivo -= 1
    digito2 = (resultado_digito2 * 10) % 11

    digito2 = digito2 if digito2 <= 9 else 0

    cpf_calculo = f'{nove_digitos}{digito1}{digito2}'

    print(cpf_calculo)