"""Desafio Imagine que você trabalha para uma empresa de telecomunicações e é responsável por validar se um número de
telefone fornecido pelo cliente está em um formato correto. Para garantir a precisão dos registros, é essencial que
os números de telefone estejam no formato padrão. Desenvolva uma função programa que valide se um número de telefone
tem o formato correto.

Formato esperado: O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9.
Lembre-se de respeitar os espaços entre os números quando preciso.

Entrada
Uma string representando o número de telefone.

Saída
Uma mensagem indicando se o número de telefone é válido ou inválido."""

import re


def validate_numero_telefone(phone_num):
    pattern = r'[(][0-9]{2}[)][ ][9][0-9]{4}[-][0-9]{4}'

    if re.match(pattern, phone_num):
        return 'Número de telefone válido.'
    else:
        return 'Número de telefone inválido.'


phone_number = input()

result = validate_numero_telefone(phone_number)

print(result)
