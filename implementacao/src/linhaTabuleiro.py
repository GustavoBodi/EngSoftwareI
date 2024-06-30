from peca import Peca
from posicao import Posicao
from cemiterio import Cemiterio
from jogador import Jogador


class LinhaTabuleiro:
    def __init__(self) -> None:
        self.__posicoes: list[Posicao] = [Posicao() for i in range(25)]
        self.__retiradas: list[Peca] = []
        self.__cemiterio_vermelhas: Cemiterio = Cemiterio(0)
        self.__cemiterio_brancas: Cemiterio = Cemiterio(1)
        self.__removida: Peca = None

    def removerPecas(self) -> None:
        for pos in self.__posicoes:
            pos.removerPecas()
        self.__retiradas.clear()
        self.__cemiterio_brancas.removerPecas()
        self.__cemiterio_vermelhas.removerPecas()

    def posicionaPecas(self, jogador, posicao: int, quantidade: int) -> list[Peca]:
        pecas_retorno = []
        for _ in range(quantidade):
            cor = jogador.obterCor()
            peca = Peca(cor)
            pecas_retorno.append(peca)
            self.adicionarPeca(peca, posicao)

        jogador.atribuirPecas(pecas_retorno)
        return pecas_retorno

    def moverPeca(self, peca: Peca, posicao: int) -> None:
        self.removerPeca(peca)
        if posicao <= 23:
            self.__posicoes[posicao].adicionarOcupante(peca)
        elif posicao == 25:
            if peca.vermelha():
                self.__cemiterio_vermelhas.adicionarPeca(peca)
            elif peca.branca():
                self.__cemiterio_brancas.adicionarPeca(peca)

    def removerPeca(self, peca: Peca) -> None:
        for pos in self.__posicoes:
            pecas = pos.obterOcupantes()
            if (peca in pecas):
                pecas.remove(peca)
                return
        if peca in self.__cemiterio_vermelhas.obterPecas():
            self.__cemiterio_vermelhas.removerPeca(peca)
        if peca in self.__cemiterio_brancas.obterPecas():
            self.__cemiterio_brancas.removerPeca(peca)

    def obterPecasCemiterioVermelho(self) -> list[Peca]:
        return self.__cemiterio_vermelhas.obterPecas()

    def obterPecasCemiterioBranco(self) -> list[Peca]:
        return self.__cemiterio_brancas.obterPecas()

    def matarPeca(self, peca: Peca) -> None:
        self.moverPeca(peca, 25)

    def pecasJogador(self, posicao: int, jogador: int) -> int:
        pecas = self.__posicoes[posicao].obterOcupantes()
        if (len(pecas) > 0 and pecas[0].cor() == jogador):
            return len(pecas)
        return 0

    def marcarRemovida(self, peca: Peca) -> None:
        self.__removida = peca

    def pecaMarcadaRemovida(self) -> Peca:
        return self.__removida

    def pecasSairam(self, cor: int) -> bool:
        for peca in self.__retiradas:
            if peca.obterCor() == cor:
                return True
        return False

    def podeSair(self, cor: int) -> bool:
        quantidade = 0
        for retirada in self.__retiradas:
            if retirada.cor() == cor:
                quantidade += 1
        if cor == 0:
            for i, posicao in enumerate(self.__posicoes):
                for peca in posicao.obterOcupantes():
                    if i >= 18:
                        quantidade += 1
        if cor == 1:
            for i, posicao in enumerate(self.__posicoes):
                for peca in posicao.obterOcupantes():
                    if i < 6:
                        quantidade += 1
        return quantidade == 15

    def adicionarPeca(self, peca: Peca, posicao: int) -> None:
        self.__posicoes[posicao].adicionarOcupante(peca)

    def obterPecas(self, posicao: int) -> list[Peca]:
        return self.__posicoes[posicao].obterOcupantes()

    def obterPosicoes(self) -> list[Posicao]:
        return self.__posicoes

    def obterPosicao(self, peca: Peca) -> int:
        for i, posicao in enumerate(self.__posicoes):
            if peca in posicao.obterOcupantes():
                return i

    def obterPecasPosicao(self, posicao: int) -> list[Peca]:
        if posicao <= 23:
            return self.__posicoes[posicao].obterOcupantes()
        else:
            raise NotImplementedError()

    def obterPecasRemovidas(self) -> list[Peca]:
        return self.__retiradas

    def sentidoPontuacao(self, peca: int, posicao: int, jogador: Jogador) -> bool:
        return peca > posicao and jogador.obterCor() == 0 or peca < posicao and jogador.obterCor() == 1
