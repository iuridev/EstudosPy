"""_summary_
DESAFIO
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

Entrada
A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

Saída
A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".
"""


T = input()
''' 
    TODO Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
    Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET"
'''

if len(T) > 140:
    print("MUTE")
else:
    print("TWEET")
