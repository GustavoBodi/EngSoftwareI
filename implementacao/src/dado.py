from random import choice


class Dado:
    def __init__(self, playerInterface) -> None:
        self.__valores: list[int] = []
        self.__playerInterface = playerInterface
        self.__inicial = True

    def zerarDados(self) -> None:
        self.__valores.clear()
        self.__inicial = True
        self.atualizarDadoInterface()

    def gerarNumero(self) -> int:
        num = choice(range(1, 7, 1))
        self.__valores.append(num)

        if len(self.__valores) == 2:
            self.__inicial = False

        self.atualizarDadoInterface()
        return num

    def duplicarDados(self) -> None:
        temp = []
        for dado in self.__valores:
            temp.append(dado)
        for dado in temp:
            self.__valores.append(dado)

        self.atualizarDadoInterface()

    def removerDado(self, valor: int) -> None:
        self.__valores.remove(valor)
        if len(self.__valores) == 0:
            self.__inicial = True
        self.atualizarDadoInterface()

    def atualizarDadoInterface(self) -> None:
        self.__playerInterface.atualizarDados(self.obterValores())

    def obterValores(self) -> list[int]:
        return self.__valores
