class Locadora:
    _locadoras = []

    def __init__(self, name) -> None:
        self._name = name
        self._ativo = False
        Locadora._locadoras.append(self)
        pass

    def __str__(self):
        _alterado = "Novo Valor" + self._name
        return print(f"{_alterado}")

    @classmethod
    def List_Locadoras(cls):
        print("--- LISTA DE LOCADORAS ---")
        print(f"{'Nome da Locadora'.ljust(25)} | {'Status do Cadastro'}")
        for loc in cls._locadoras:
            # print(vars(loc))
            # loc.ativo vai ativar a @property
            print(f"{loc._name.ljust(25)} | {loc.ativo}")

    def altera_estado(self):
        self._ativo = not self._ativo

    def altera_nome(self, new_name):
        self._name = new_name

    @property
    def ativo(self):
        return "ativado" if self._ativo else "desativado"


# corpo :

locadora_1 = Locadora("LocaWeb")
locacora_2 = Locadora("LocaMAX")
locadora_3 = Locadora("NetFlix")

Locadora.List_Locadoras()
locacora_2.altera_estado()

Locadora.List_Locadoras()

locadora_3.altera_nome("NewFlix")
Locadora.List_Locadoras()
