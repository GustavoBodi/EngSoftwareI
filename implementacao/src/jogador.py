from peca import Peca
from linhaTabuleiro import LinhaTabuleiro
from dado import Dado
from tabuleiro import Tabuleiro


class Jogador:
    def __init__(self, tabuleiro: Tabuleiro, linhaTabuleiro: LinhaTabuleiro, dado: Dado) -> None:
        self.__nome: str = ""
        self.__cor: int = 0
        self.__seuTurno: bool = False
        self.__vencedor: bool = False
        self.__turnoPossivel: bool = False
        self.__pecas: list[Peca] = []
        self.__valorMovimento: int = 0
        self.__sentido: bool = False
        self.__tabuleiro: Tabuleiro = tabuleiro
        self.__linhaTabuleiro: LinhaTabuleiro = linhaTabuleiro
        self.__dado: Dado = dado

    def suaPosicao(self, posicao: int) -> bool:
        pecas = self.__linhaTabuleiro.obterPecas(posicao)
        if len(pecas) > 0:
            if pecas[0].branca() and self.obterCor() == 0:
                return True
            elif pecas[0].vermelha() and self.obterCor() == 1:
                return False

    def registraPosicao(self, posicao: int) -> None:
        raise NotImplementedError()

    def definirTurnoPossivel(self) -> None:
        self.__turnoPossivel = True

    def definirTurnoTerminado(self) -> None:
        self.__seuTurno = False

    def inicializar(self) -> None:
        raise NotImplementedError()

    def habilitaTurno(self) -> None:
        self.__seuTurno = True

    def copiarDados(self, dados: list[int]) -> list[int]:
        temp = []
        for dado in dados:
            temp.append(dado)
        return temp

    def avaliarPossibilidadeTurno(self) -> bool:
        dados = self.__tabuleiro.obterDado()

        for dado in dados:
            for peca in self.__pecas:
                for posicao in range(0, 25):
                    movimentoPossivel = self.__tabuleiro.avaliarMovimento(peca, posicao, dado)
                    if movimentoPossivel:
                        self.marcarMovimentoPossivel()
                        return True

        self.marcarMovimentoImpossivel()
        return False

    def copiarPecas(self, pecas: list[Peca]) -> list[Peca]:
        temp = []
        for peca in self.__pecas:
            temp.append(peca)
        return temp

    def marcarMovimentoPossivel(self) -> None:
        self.__turnoPossivel = True

    def marcarMovimentoImpossivel(self) -> None:
        self.__turnoPossivel = False

    def limparTabuleiro(self) -> None:
        self.__linhaTabuleiro.removerPecas()

    def atribuirPecas(self, pecas: list[Peca]) -> None:
        self.__pecas = pecas

    def obterValorMovimento(self) -> None:
        raise NotImplementedError()

    def acabaramPecas(self) -> bool:
        pecas_removidas = self.__linhaTabuleiro.obterPecasRemovidas()
        pecas = []
        for peca in pecas_removidas:
            if peca.branca() and self.obterCor() == 0:
                pecas.append(peca)
            elif peca.vermelha() and self.obterCor() == 1:
                pecas.append(peca)
        return len(pecas) == 15

    def habilitarComoVencedor(self) -> None:
        self.__vencedor = True

    def sentidoPontuacao(self, peca: Peca, posicao: int) -> bool:
        posicao_atual = self.__linhaTabuleiro.obterPosicao(peca)
        if posicao_atual > posicao and self.obterCor() == 0:
            return True
        elif posicao_atual < posicao and self.obterCor() == 1:
            return True
        return False

    def inicializar(self, nome: str, cor: int, identificador: str) -> None:
        raise NotImplementedError()

    def obterCor(self) -> int:
        return self.__cor

    def obterCorAdversario(self) -> int:
        if self.__cor == 1:
            return 0
        else:
            return 0
