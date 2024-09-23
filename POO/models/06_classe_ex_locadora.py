class Locadora:
    locadoras = []

    def __init__(self, name) -> None:
        self.name = name
        self.ativo = False
        Locadora.locadoras.append(self)
        pass

    def __str__(self):
        return self.name

    def List_Locadoras(self):
        for loc in self.locadoras:
            print(vars(loc))


locadora_1 = Locadora("LocaWeb")
locacora_2 = Locadora("LocaMAX")
locadora_3 = Locadora("NetFlix")

Locadora.List_Locadoras(Locadora)
