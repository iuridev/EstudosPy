'''
Descrição
Neste desafio, o objetivo ajudar na escolha do modelo de inteligência artificial mais adequado com base em critérios específicos definidos pelo cliente, utilizando as inovações recentemente anunciadas pela Amazon Web Services (AWS). Os modelos de IA disponíveis são da família Claude 3, desenvolvidos pela Anthropic, que foram anunciados como disponíveis na plataforma Amazon Bedrock. Esses modelos de última geração foram projetados para oferecer um equilíbrio entre precisão, desempenho, velocidade e custo, atendendo às demandas de clientes de todos os tamanhos.

Atenção:
Alguns dados que utilizados são simulados e podem não representar situações reais.

Entrada
A entrada consiste em quatro linhas, cada uma representando uma característica do modelo de inteligência artificial:

1. Desempenho: um número inteiro indicando a capacidade de desempenho do modelo.
2. Velocidade: um número inteiro representando a velocidade de processamento do modelo.
3. Custo: um número inteiro que reflete o custo associado ao modelo.
4. Capacidades: uma lista de capacidades específicas separadas por vírgulas.

Saída
O programa fornecerá a recomendação do modelo mais adequado com base nas características fornecidas. A saída incluirá uma explicação detalhada sobre por que esse modelo específico foi escolhido com base nos critérios estabelecidos pelo cliente, utilizando informações sobre os modelos Claude 3 disponíveis na plataforma Amazon Bedrock. Se nenhum modelo atender aos critérios, o programa informará que nenhum modelo foi encontrado.
'''


class ModeloIA:
    def __init__(self, nome, desempenho, velocidade, custo, capacidades):
        self.nome = nome
        self.desempenho = desempenho
        self.velocidade = velocidade
        self.custo = custo
        self.capacidades = capacidades

    def __str__(self):
        return self.nome


modelos = [
    ModeloIA("Claude 3 Opus", 9, 10, 5, [
             "pesquisa", "desenvolvimento acelerado"]),
    ModeloIA("Claude 3 Sonnet", 8, 5, 7, [
             "codificação", "recuperação de informações"]),
    ModeloIA("Claude 3 Haiku", 7, 9, 6, [
             "velocidade", "resumo de dados não estruturados"])
]


def recomendar_modelo(caracteristicas):
    modelo_recomendado = None
  # Aqui é convertido as capacidades inseridas pelo usuário para minúsculas:
    capacidades_usuario = [capacidade.lower()
                           for capacidade in caracteristicas['Capacidades']]

    for modelo in modelos:
        # Convertemos as capacidades do modelo para minúsculas:
        capacidades_modelo = [capacidade.lower()
                              for capacidade in modelo.capacidades]

        if all(capacidade in capacidades_usuario for capacidade in capacidades_modelo):
            if modelo_recomendado is None or modelo.desempenho > modelo_recomendado.desempenho:
                modelo_recomendado = modelo

    return modelo_recomendado if modelo_recomendado else "Nenhum modelo encontrado."

# Aqui temos a função que gera uma explicação para o modelo recomendado:


def gerar_explicacao(modelo, caracteristicas):
    if isinstance(modelo, ModeloIA):
        explicacao = f"O {modelo.nome} é o modelo recomendado."
        return explicacao
    else:
        return modelo

# Aqui fica a função que solicita características desejadas ao usuário:


def obter_caracteristicas():
    caracteristicas = {}
    caracteristicas['Desempenho'] = int(input())
    caracteristicas['Velocidade'] = int(input())
    caracteristicas['Custo'] = int(input())
    capacidades = input().split(',')
    caracteristicas['Capacidades'] = [capacidade.strip()
                                      for capacidade in capacidades]
    return caracteristicas


caracteristicas_entrada = obter_caracteristicas()
melhor_modelo = recomendar_modelo(caracteristicas_entrada)
explicacao = gerar_explicacao(melhor_modelo, caracteristicas_entrada)

print(explicacao)
