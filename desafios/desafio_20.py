'''
Desafio
Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano. Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada' para gerar uma mensagem personalizada.

Condições da verificação do saldo:
- Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
- Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
- Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

Entrada
Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

Saída
Mensagem personalizada de acordo o saldo do cliente.
'''


class PlanoTelefone:
    def __init__(self, nome_plano, saldo):
        self._nome_plano = nome_plano
        self._saldo = saldo
        pass

    def mensagem_personalizada(self, saldo):
        if saldo < 10:
            return 'Seu saldo está baixo. Recarregue e use os serviços do seu plano.'
        elif saldo >= 50:
            return 'Parabéns! Continue aproveitando seu plano sem preocupações.'
        else:
            return 'Seu saldo está razoável. Aproveite o uso moderado do seu plano.'


class UsuarioTelefone:
    def __init__(self, nome, plano: PlanoTelefone):
        self.nome = nome
        self.plano = plano

    def verificar_saldo(self):
        saldo = self.plano._saldo
        return saldo, self.plano.mensagem_personalizada(saldo)


nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)

saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
print(mensagem_usuario)
