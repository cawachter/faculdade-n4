class Calculadora:
    def __init__(self, valorA, valorB, operacao):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self, operacao):
        simbolos_validos = {'+', '-', '*', '/'}
        return operacao in simbolos_validos

    def calcular(self):
        if self.validarOperacao(self.__operacao):
            if self.__operacao == "/":
                if valorA == 0 or valorB == 0:
                    print("Impossível dividir por zero.")
                    return
                else: 
                    return self.__valorA / self.__valorB

            elif self.__operacao == "+":
                return self.__valorA + self.__valorB
            elif self.__operacao == "-":
                return self.__valorA - self.__valorB
            elif self.__operacao == "*":
                return self.__valorA * self.__valorB
        else:
            print("Operação inválida!")
            return

    def mostrarResultado(self):
        print(str(self.__valorA) + ' ' + self.__operacao + ' ' + str(self.__valorB) + ' = ' + str(self.calcular()))

