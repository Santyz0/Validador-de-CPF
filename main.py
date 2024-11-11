import re
import sys

entrada = input('Digite um CPF: ')
cpf = re.sub(r'[^0-9]', '', entrada)

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print(f'Você digitou um CPF({entrada}) sequencial')
    sys.exit()

nove_digitos = cpf[:9]
dez_digitos = cpf[:10]
contador_regressivo1 = 10
contador_regressivo2 = 11

total1 = 0
total2 = 0

for numero in nove_digitos:
   
    total1 += int(numero) * contador_regressivo1

    contador_regressivo1 -= 1
    
valor_digito1 = (total1 * 10) % 11


digito_um = 0 if valor_digito1 > 9 else valor_digito1
digito_um_str = str(digito_um)


for numeros in dez_digitos:
    total2 += int(numeros) * contador_regressivo2
    contador_regressivo2 -= 1

valor_digito2 = (total2 * 10) % 11

digito_dois = 0 if valor_digito2 > 9 else valor_digito2
digito_dois_str = str(digito_dois)

cpf_completo = f'{nove_digitos}{digito_um}{digito_dois}'

if cpf == cpf_completo:
    print(f'Seu CPF(->{cpf}<-) é válido')
else:
    print(f'Seu CPF(->{entrada}<-) não constou no sistema')