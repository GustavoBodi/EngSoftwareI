from peca import Peca

class Cemiterio:
    def __init__(self, cor: int) -> None:
        self.__pecas: list[Peca] = []
        self.__cor: int = cor

    def removerPecas(self) -> None:
        raise NotImplementedError()

    def adicionarPeca(self, peca: Peca) -> None:
        raise NotImplementedError()

    def existePecaCemiterio(self) -> bool:
        raise NotImplementedError()

    def obterPecas(self) -> list[Peca]:
        raise NotImplementedError()
