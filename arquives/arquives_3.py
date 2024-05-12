from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open('arquivo_fechamento_auto.txt', 'w', encoding='utf-8') as arq:
        arq.write("escrevendo no arquivo 4")
except IOError:
    print("Não foi possivel abri o arquivo")



try:
    with open('arquivo_fechamento_auto.txt', 'r', encoding='utf-8') as arq:
        print(arq.read())
except IOError:
    print("Não foi possivel abri o arquivo")
