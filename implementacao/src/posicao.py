from peca import Peca

class Posicao:
    def __init__(self) -> None:
        self.__ocupantes: list[Peca] = []

    def removerPecas(self) -> None:
        raise NotImplementedError()

    def removerPeca(self, peca: Peca) -> None:
        raise NotImplementedError()

    def obterOcupantes(self) -> list[Peca]:
        raise NotImplementedError()
