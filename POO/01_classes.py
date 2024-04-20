class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print( "Plim, Plim plim...")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
    def __del__(self):
        print('objeto sendo deletado!')


bike1 = bicicleta("preta","caloi",2011, 850)
bike2 = bicicleta("azul","brazu",2020, 700)


bike1.buzinar()

bicicleta.buzinar(bike2)

print(bike2)
print(bike1)