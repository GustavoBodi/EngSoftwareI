from jogador import Jogador
from peca import Peca
from posicao import Posicao
from cemiterio import Cemiterio


class LinhaTabuleiro:
    def __init__(self) -> None:
        self.__posicoes: list[Posicao] = [Posicao() for i in range(25)]
        self.__retiradas: list[Peca] = []
        self.__cemiterio_vermelhas: Cemiterio = Cemiterio()
        self.__cemiterio_brancas: Cemiterio = Cemiterio()
        self.__removida: Peca = None

    def removerPecas(self) -> None:
        for pos in self.__posicoes:
            pos.removerPecas()

    def posicionaPecas(self, jogador: int, posicao: int, quantidade: int) -> list[Peca]:
        pecas_retorno = []
        for i in range(quantidade):
            peca = Peca(jogador)
            pecas_retorno.append(peca)
            self.__posicoes[posicao].adicionarOcupante(peca)
        return pecas_retorno

    def moverPeca(self, peca: Peca, posicao: int) -> None:
        for pos in self.__posicoes:
            pecas = pos.obterOcupantes()

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
        self.__removida = peca

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
