from abc import ABC
from abc import ABCMeta, abstractmethod


class pessoa(ABC):  #informa que a classe é abstrata

    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def idade(self):
        pass


class brasileiro(pessoa):

    def nome(self):
        print("Nome")
    
    def idade(self):
        print("Idade")

    
br1 = brasileiro()
print(br1.nome())
print(br1.idade())
