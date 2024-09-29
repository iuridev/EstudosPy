class Locadora:
    _locadoras = []

    def __init__(self, name) -> None:
        self._name = name
        self._ativo = False
        Locadora._locadoras.append(self)
        pass

    def __str__(self):
        return self._name

    def List_Locadoras(self):
        print("--- LISTA DE LOCADORAS ---")
        for loc in self._locadoras:
            # print(vars(loc))
            # loc.ativo vai ativar a @property
            print(f"Biblioteca: {loc._name} | {loc.ativo}")

    def altera_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return "ativado" if self._ativo else "desativado"


locadora_1 = Locadora("LocaWeb")
locacora_2 = Locadora("LocaMAX")
locadora_3 = Locadora("NetFlix")

Locadora.List_Locadoras(Locadora)
locacora_2.altera_estado()

Locadora.List_Locadoras(Locadora)
