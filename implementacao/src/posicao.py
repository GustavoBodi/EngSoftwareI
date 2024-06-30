from peca import Peca


class Posicao:
    def __init__(self) -> None:
        self.__ocupantes: list[Peca] = []

    def removerPecas(self) -> None:
        self.__ocupantes.clear()

    def removerPeca(self) -> None:
        self.__ocupantes.pop()

    def obterOcupantes(self) -> list[Peca]:
        return self.__ocupantes

    def adicionarOcupante(self, peca: Peca):
        self.__ocupantes.append(peca)

    def quantidadeOcupantes(self) -> int:
        return len(self.__ocupantes)
