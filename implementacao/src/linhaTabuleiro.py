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
            self.adicionarPeca(peca, posicao)
        return pecas_retorno

    def moverPeca(self, peca: Peca, posicao: int) -> None:
        self.removerPeca(peca)
        self.__posicoes[posicao].adicionarOcupante(peca)

    def retirarPecaTabuleiro(self, peca: Peca) -> None:
        self.removerPeca(peca)
        self.__removida.append(peca)

    def removerPeca(self, peca: Peca) -> int:
        for pos in self.__posicoes:
            pecas = pos.obterOcupantes()
            if (peca in pecas):
                pecas.remove(peca)
                break

    def moverForaTabuleiro(self, peca: Peca) -> None:
        self.retirarPecaTabuleiro(peca)

    def matarPeca(self, peca: Peca) -> None:
        self.retirarPecaTabuleiro(peca)
        if peca.vermelha():
            self.__cemiterio_vermelhas.adicionarPeca(peca)
        else:
            self.__cemiterio_brancas.adicionarPeca(peca)

    def pecasAdversario(self, posicao: int, adversario: int) -> int:
        pos: Posicao = self.__posicoes[posicao]
        pecas: list[Peca] = pos.obterOcupantes()
        if (pecas[0].vermelha() and adversario == 1) or (pecas[0].branca() and adversario == 0):
            return len(pecas)
        return 0

    def marcarRemovida(self, peca: Peca) -> None:
        self.__removida = peca

    def pecasSairam(self, jogador: Jogador) -> bool:
        cor: int = jogador.obterCor()
        for peca in self.__retiradas:
            if peca.branca() and cor == 0:
                return True
            if peca.vermelha() and cor == 1:
                return True
        return False

    def adicionarPeca(self, peca: Peca, posicao: int) -> None:
        self.__posicoes[posicao].adicionarOcupante(peca)

    def removerPecaTabuleiro(self, peca: Peca) -> None:
        self.retirarPecaTabuleiro(peca)

    def obterPecas(self, posicao: int) -> list[Peca]:
        return self.__posicoes[posicao].obterOcupantes()

    def obterPosicoes(self) -> list[Posicao]:
        return self.__posicoes

    def obterPosicao(self, peca: Peca) -> int:
        for i, posicao in enumerate(self.__posicoes):
            if peca in posicao.obterOcupantes():
                return i

    def obterPecasRemovidas(self) -> list[Peca]:
        return self.__retiradas
