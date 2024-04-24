class pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
        self.ano_nascimento = 2024 - idade

    @classmethod
    def Criar_Pessoa(cls, nome, ano_nascimento):
        cls.nome = nome
        cls.ano_nascimento = ano_nascimento
        cls.idade = 2024 - ano_nascimento
        print(cls.nome, cls.idade, cls.ano_nascimento)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18

P1 = pessoa("Iuri Barreto", 29)
print(P1.nome, P1.idade, P1.ano_nascimento)


P2 = pessoa.Criar_Pessoa("Maria Eduarda", 1994)

print(P1.maior_idade(P1.idade))

