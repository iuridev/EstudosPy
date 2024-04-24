#Sistema de Banco com conhecimento adquiridos de POO em python
from datetime import date
from abc import ABC
from abc import abstractmethod
from project_03 import Historico, Transacao


class Cliente():
    _endereço : str
    _contas : list
    def realizar_transacao():
        pass

    def add_conta():
        pass

class Pessoa_Fisica(Cliente):
    _cpf : str
    _nome : str
    _data_nascimento: date
    def __init__(self, cpf: str, nome:str, data_nascimento:date) -> None:
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento



class Conta():
    _saldo: float
    _numero: int
    _agencia: str
    _cliente: Cliente
    _historico: Historico


    def saldo(self):
        return self._saldo

    def nova_conta(self, cliente:Cliente, num:int):
        self._cliente = cliente
        self._numero = num
        

    def sacar(self, valor:float):
        sacar = Sacar(valor)
        self._historico.add_transacao(sacar, self, valor)

    def depositar(self, valor:float):
        dep = Depositar(valor)
        self._historico.add_transacao(dep, self, valor)



class Transacao(ABC):
    @abstractmethod
    def registrar(cls, conta : Conta):
        pass

class Sacar(Transacao):
    _valor : float
    def registrar(cls, conta: Conta, saque:float):
        cls._valor = saque

class Depositar(Transacao):
    _valor : float
    def registrar(cls, conta: Conta, deposito:float):
        cls._valor = deposito

class Historico():
    def add_transacao(self, transacao:Transacao, conta : Conta, valor:float):
        return transacao.registrar(conta, valor )
    
class conta_correte(Conta):
    _limite : float
    _limite_saque : int