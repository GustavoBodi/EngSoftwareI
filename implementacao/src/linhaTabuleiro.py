from jogador import Jogador
from peca import Peca
from posicao import Posicao

class LinhaTabuleiro:
    def __init__(self) -> None:
        self.__posicoes: list[Posicao] = [];
        self.__retiradas: list[Peca] = [];

    def removerPecas(self) -> None:
        raise NotImplementedError()

    def posicionaPecas(self, jogador: int, posicao: int, quantidade: int) -> list[Peca]:
        raise NotImplementedError()

    def moverPeca(self, peca: Peca, posicao: int) -> None:
        raise NotImplementedError()

    def retirarPecaTabuleiro(self, peca: Peca) -> None:
        raise NotImplementedError()

    def removerPeca(self, peca: Peca) -> None:
        raise NotImplementedError()

    def moverForaTabuleiro(self, peca: Peca) -> None:
        raise NotImplementedError()

    def matarPeca(self, peca: Peca) -> None:
        raise NotImplementedError()

    def pecasAdversario(self, posicao: int, adversario: int) -> int:
        raise NotImplementedError()

    def marcarRemovida(self, peca: Peca) -> None:
        raise NotImplementedError()

    def pecasSairam(self, jogador: Jogador) -> bool:
        raise NotImplementedError()

    def adicionarPeca(self, peca: Peca, posicao: int) -> None:
        raise NotImplementedError()

    def removerPecaTabuleiro(self, peca: Peca) -> None:
        raise NotImplementedError()

    def obterPosicoes(self) -> list[Posicao]:
        raise NotImplementedError()

    def obterPecasRemovidas(self) -> list[Peca]:
        raise NotImplementedError()
