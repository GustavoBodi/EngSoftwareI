from peca import Peca


class Jogador:
    def __init__(self, nome: str, cor: int, identificador: str) -> None:
        self.__nome: str = nome
        self.__cor: int = cor
        self.__identificador: str = identificador
        self.__seuTurno: bool = False
        self.__vencedor: bool = False
        self.__turnoPossivel: bool = False
        self.__pecas: list[Peca] = []
        self.__valorMovimento: int = 0
        self.__sentido: bool = False

    def habilitaTurno(self) -> None:
        self.__seuTurno = True

    def definirTurnoTerminado(self) -> None:
        self.__seuTurno = False

    def marcarMovimentoPossivel(self) -> None:
        self.__turnoPossivel = True

    def marcarMovimentoImpossivel(self) -> None:
        self.__turnoPossivel = False

    def limparTabuleiro(self) -> None:
        self.removerPecas()

    def removerPecas(self) -> None:
        self.__pecas.clear()

    def removerPeca(self, peca: Peca) -> None:
        self.__pecas.remove(peca)

    def atribuirPecas(self, pecas: list[Peca]) -> None:
        self.__pecas = pecas

    def obterValorMovimento(self) -> None:
        raise NotImplementedError()

    def acabaramPecas(self) -> bool:
        return len(self.__pecas == 0)

    def habilitarComoVencedor(self) -> None:
        self.__vencedor = True

    def obterCor(self) -> int:
        return self.__cor

    def obterCorAdversario(self) -> int:
        if self.__cor == 1:
            return 0
        else:
            return 0
