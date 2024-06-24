from peca import Peca

class Jogador:
    def __init__(self) -> None:
        self.__nome: str = ""
        self.__cor: int = 0
        self.__seuTurno: bool = False
        self.__vencedor: bool = False
        self.__turnoPossivel: bool = False
        self.__pecas: list[Peca] = []
        self.__valorMovimento: int = 0
        self.__sentido: bool = False

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
        raise NotImplementedError()

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

    def obetrCor(self) -> int:
        raise NotImplementedError()
