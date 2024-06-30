from peca import Peca


class Cemiterio:
    def __init__(self, cor: int) -> None:
        self.__pecas: list[Peca] = []
        self.__cor: int = cor

    def removerPecas(self) -> None:
        self.__pecas.clear()

    def removerPeca(self, peca: Peca) -> None:
        for peca_interna in self.__pecas:
            if peca_interna == peca:
                self.__pecas.remove(peca)

    def adicionarPeca(self, peca: Peca) -> None:
        self.__pecas.append(peca)

    def adicionar(self) -> None:
        self.__pecas.append(Peca(self.__cor))

    def existePecaCemiterio(self) -> bool:
        return len(self.__pecas) > 0

    def obterPecas(self) -> list[Peca]:
        return self.__pecas
