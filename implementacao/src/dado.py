class Dado:
    def __init__(self) -> None:
        self.__valores: list[int] = []

    def zerarDados(self) -> None:
        raise NotImplementedError()

    def gerarNumero(self) -> int:
        raise NotImplementedError()

    def duplicarDados(self) -> None:
        raise NotImplementedError()

    def removerDado(self, valor: int) -> None:
        raise NotImplementedError()

    def atualizarDadoInterface(self) -> None:
        raise NotImplementedError()

    def obterValores(self) -> list[int]:
        raise NotImplementedError()
