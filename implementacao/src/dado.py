from random import choice


class Dado:
    def __init__(self) -> None:
        self.__valores: list[int] = []

    def zerarDados(self) -> None:
        self.__valores.clear()

    def gerarNumero(self) -> int:
        num = choice(range(1, 7, 1))
        self.__valores.append(num)
        return num

    def duplicarDados(self) -> None:
        temp = []
        for dado in self.__valores:
            temp.append(dado)
        for dado in temp:
            self.__valores.append(dado)

    def removerDado(self, valor: int) -> None:
        self.__valores.remove(valor)

    def atualizarDadoInterface(self) -> None:
        raise NotImplementedError()

    def obterValores(self) -> list[int]:
        return self.__valores
