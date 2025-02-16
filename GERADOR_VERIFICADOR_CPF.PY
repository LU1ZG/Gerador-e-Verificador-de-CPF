import random
import os
import re

nove_digitos = ''

while True:
    print('***Gerador e Validador de CPF***')
    entrada = input('[G]erar CPF - [V]erificar CPF - [S]air: ').upper()
    nove_digitos = ''
    
    if entrada == 'G':
    
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

        contator_regressivo_1 = 10
        calculo_digito_1 = 0

        # Calculo do primeiro digito do CPF.

        for digito_1 in nove_digitos:
            calculo_digito_1 += int(digito_1) * contator_regressivo_1
            contator_regressivo_1 -= 1

        resultado_digito_1 = (calculo_digito_1 * 10) % 11  
        primeiro_digito = 0 if resultado_digito_1 > 9 else resultado_digito_1

        # Calculo do segundo digito do CPF.

        dez_digitos = nove_digitos + str(primeiro_digito)
        contator_regressivo_2 = 11
        calculo_digito_2 = 0

        for digito_2 in dez_digitos:
            calculo_digito_2 += int(digito_2) * contator_regressivo_2
            contator_regressivo_2 -= 1

        resultado_digito_2 = (calculo_digito_2 * 10) % 11 
        segundo_digito = 0 if resultado_digito_2 > 9 else resultado_digito_2

        cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
        os.system('cls')
        print(f'O CPF {cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:11]} foi gerado!')

    if entrada == 'V':

        os.system('cls')
        entrada_2 = input('Digite um CPF: ')
        cpf_usuario = re.sub(r'[^0-9]','', entrada_2)
        valores_sequenciais = entrada_2 == entrada_2[0] * len(entrada_2)

        if valores_sequenciais:
            os.system('cls')
            print('Você enviou dados sequenciais!')
            continue

        # Calculo do primeiro digito do CPF.
        
        nove_digitos = cpf_usuario[:9]
        contator_regressivo_1 = 10
        calculo_digito_1 = 0

        for digito_1 in nove_digitos:
            calculo_digito_1 += int(digito_1) * contator_regressivo_1
            contator_regressivo_1 -= 1

        resultado_digito_1 = (calculo_digito_1 * 10) % 11
        primeiro_digito = 0 if resultado_digito_1 > 9 else resultado_digito_1

        # Calculo do segundo digito do CPF.

        dez_digitos = nove_digitos + str(primeiro_digito)
        contator_regressivo_2 = 11
        calculo_digito_2 = 0

        for digito_2 in dez_digitos:
            calculo_digito_2 += int(digito_2) * contator_regressivo_2
            contator_regressivo_2 -= 1

        resultado_digito_2 = (calculo_digito_2 * 10) % 11 
        segundo_digito = 0 if resultado_digito_2 > 9 else resultado_digito_2

        cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

        if cpf_gerado == cpf_usuario:
            os.system('cls')
            print(f'O CPF {cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:11]} é valido!')
        else:
            os.system('cls')
            print('CPF invalido!')
    
    if entrada == 'S':
        os.system('cls')
        print('Você saiu do programa!')
        break