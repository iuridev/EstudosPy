'''
    args - usa-se quando não sabemos quantos argumentos queremos ter uma função
        os argumentos são passados como uma tupla.
        para caracterizar usa-se o sinal de '*'
'''


def sum(*num):
    sum_total = 0
    for i in num:
        sum_total += i
    print(f"O resultado da soma é : {sum_total}")


sum(23, 20, 40)


'''
    kwargs - Além dos valores podemos passar chave para cada argumento
        os argumentos são passados como dicionário.
        para caracterizar usa-se o sinal de '**'
'''


def curso(**data):
    for key, value in data.items():
        print(f"{key}: {value}")


curso(name='Python', duration='1 year')
