'''
    Exemplo: Biblioteca
'''


class Biblioteca:
    name = ""
    ativa = False


biblioteca_1 = Biblioteca()
biblioteca_1.name = "Barreto Lib"
biblioteca_1.ativa = True

biblioteca_2 = Biblioteca()
biblioteca_2.name = "GuaruLiv"
biblioteca_2.ativa = False

bibliotecas = [biblioteca_1, biblioteca_2]

for biblioteca in bibliotecas:
    print(vars(biblioteca))
