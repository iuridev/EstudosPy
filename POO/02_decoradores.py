class humam:
    #encapsulamento privado
    #no python apenas conceito
    def __init__(self, nome) -> None:
        self._nome = nome
    

    @property      #decorador
    def name(self):
        return self._nome or any
    
    @name.setter
    def name(self, value):
        self._nome = value or any


humam01 = humam("Iuri")

print(humam01.name)