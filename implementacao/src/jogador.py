from peca import Peca
from tabuleiro import Tabuleiro

class Jogador:
    def __init__(self, tabuleiro: Tabuleiro) -> None:
        self.__nome: str = ""
        self.__cor: int = 0
        self.__seuTurno: bool = False
        self.__vencedor: bool = False
        self.__turnoPossivel: bool = False
        self.__pecas: list[Peca] = []
        self.__valorMovimento: int = 0
        self.__sentido: bool = False
        self.__tabuleiro: Tabuleiro = tabuleiro

    def suaPosicao(self, posicao: int) -> bool:
        raise NotImplementedError()

    def registraPosicao(self, posicao: int) -> None:
        raise NotImplementedError()

    def definirTurnoPossivel(self) -> None:
        raise NotImplementedError()

    def definirTurnoTerminado(self) -> None:
        raise NotImplementedError()

    def inicializar(self) -> None:
        raise NotImplementedError()

    def habilitaTurno(self) -> None:
        raise NotImplementedError()

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

    def copiarDados(self, dados: list[int]) -> list[int]:
        raise NotImplementedError()

    def copiarPecas(self, pecas: list[Peca]) -> list[Peca]:
        raise NotImplementedError()

    def marcarMovimentoPossivel(self) -> None:
        raise NotImplementedError()

    def marcarMovimentoImpossivel(self) -> None:
        raise NotImplementedError()

    def limparTabuleiro(self) -> None:
        raise NotImplementedError()

    def atribuirPecas(self, peca: list[Peca]) -> None:
        raise NotImplementedError()

    def obterValorMovimento(self) -> None:
        raise NotImplementedError()

    def acabaramPecas(self) -> bool:
        raise NotImplementedError()

    def habilitarComoVercedor(self) -> None:
        raise NotImplementedError()

    def sentidoPontuacao(self, peca: Peca, posicao: int) -> bool:
        raise NotImplementedError()

    def inicializar(self, nome: str, cor: int, identificador: str) -> None:
        raise NotImplementedError()

    def obterCor(self) -> int:
        raise NotImplementedError()
