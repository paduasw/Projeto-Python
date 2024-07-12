import re
import sys
entrada = input('CPF [74682489070]: ')
cpf_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)
entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('você digitou numeros sequenciais')
    sys.exit

nove_digitos = cpf_usuario[:9]
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

if cpf_usuario == cpf_calculo:
    print(f'{cpf_usuario} é valido')
else:
    print('CPF inválido')