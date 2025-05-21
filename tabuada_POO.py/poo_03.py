class ContaBancaria:
    def __init__(self,titular,saldo_incial):
        self.titular = titular

        #Atributo protegido ( privado )
        self._saldo = saldo_incial

    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de {valor} realizado com sucesso. ")

        else:
            print("O valor deverá ser positivo. ")

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque no valor de {valor} realizado com sucesso. ")
        
        else:
            print(" Saldo insuficiente ou valor inválido. ")

    def consulta_saldo(self):
        print(f"O seu saldo atual é: {self._saldo}")
