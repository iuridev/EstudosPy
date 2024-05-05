"""Desafio Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes a
escolherem o plano de internet ideal com base em seu consumo mensal de dados. Para a resolução, você pode solicitar
ao usuário que insira o seu consumo, sendo este um valor 'float'. Crie uma função chamada recomendar_plano para
receber o consumo médio mensal de dados informado pelo cliente, além de utilizar estruturas condicionais para fazer a
verification e retornar o plano adequado.

Planos Oferecidos:

- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

Entrada
Como entrada solicite o consumo médio mensal de dados em GB (float).

Saída
Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.
"""


def recomendar_plano(consumo_medio: float):
    _PLAN_50 = "Plano Essencial Fibra - 50Mbps"
    _PLAN_100 = "Plano Prata Fibra - 100Mbps"
    _PLAN_300 = "Plano Premium Fibra - 300Mbps"
    _GB_LOW = 10
    _GB_HIGH = 20
    plan_ideal = ""

    if consumo_medio <= _GB_LOW:
        plan_ideal = _PLAN_50
    elif consumo_medio <= _GB_HIGH:
        plan_ideal = _PLAN_100
    else:
        plan_ideal = _PLAN_300

    return plan_ideal


# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
