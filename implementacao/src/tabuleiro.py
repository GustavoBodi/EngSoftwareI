from cemiterio import Cemiterio
from dado import Dado
from jogador import Jogador
from linhaTabuleiro import LinhaTabuleiro
from peca import Peca
from main import PlayerInterface


class Tabuleiro:
    def __init__(self) -> None:
        self.__partidaEmAndamento: bool = False
        self.__linhaTabuleiro: LinhaTabuleiro = LinhaTabuleiro()
        self.__pecas: list[Peca] = []
        self.__estadoPartida: int = 0
        self.__dados: Dado = Dado()
        self.__match_status: int = 0
        self.__jogadorLocal: Jogador
        self.__playerInterface: PlayerInterface

    def __inicializar(self, simbolo: int, id: str, nome: str) -> None:
        raise NotImplementedError()

    def adicionarPeca(self, peca: Peca, posicao: int) -> None:
        raise NotImplementedError()

    def adicionarPeca(self, peca: Peca) -> None:
        raise NotImplementedError()

    def adicionarPecaForaTabuleiro(self, peca: Peca) -> None:
        raise NotImplementedError()

    def alcancavelDados(self, peca: Peca, posicao: int, dado: int) -> bool:
        raise NotImplementedError()

    def avaliarMovimento(self, peca: Peca, posicao: int, dado: int) -> bool:
        raise NotImplementedError()

    def avaliarPossibilidadeTurno(self) -> bool:
        raise NotImplementedError()

    def avaliarTermino(self) -> bool:
        raise NotImplementedError()

    def colocaMovimentoIrregular(self) -> None:
        raise NotImplementedError()

    def colocaMovimentoOcorrendo(self) -> None:
        raise NotImplementedError()

    def colocarEsperando(self) -> None:
        raise NotImplementedError()

    def comecar_partida(self, jogadores: list[str], idJogadorLocal: str) -> None:
        raise NotImplementedError()

    def definirMovimento(self) -> None:
        raise NotImplementedError()

    def definirTurnoPossivel(self) -> None:
        raise NotImplementedError()

    def definirTerminado(self) -> None:
        raise NotImplementedError()

    def existePecaCemiterio(self) -> bool:
        raise NotImplementedError()

    def identificaJogadorTurno(self) -> Jogador:
        raise NotImplementedError()

    def jogarDados(self) -> None:
        self.__dados.zerarDados()
        valor1 = self.__dados.gerarNumero()
        valor2 = self.__dados.gerarNumero()

        if valor1 == valor2:
            self.__dados.duplicarDados()

        movimentoPossivel = self.__jogadorLocal.avaliarPossibilidadeTurno()

        if movimentoPossivel:
            self.__jogadorLocal.definirTurnoPossivel()
            self.registrarDados()
            valores = self.__dados.obterValores()
            self.__playerInterface.atualizarDados(valores)
        else:
            self.__jogadorLocal.definirTurnoTerminado()

    def limparTabuleiro(self) -> None:
        raise NotImplementedError()

    def marcarJogoTerminado(self) -> None:
        raise NotImplementedError()

    def marcarMovimento(self, estado: str) -> None:
        raise NotImplementedError()

    def marcarPontoJogador(self, jogador: Jogador) -> None:
        raise NotImplementedError()

    def marcarTerminado(self) -> None:
        raise NotImplementedError()

    def movimentoOcorrendo(self) -> bool:
        raise NotImplementedError()

    def movimentoRegular(self) -> None:
        raise NotImplementedError()

    def obterDado(self) -> list[int]:
        return self.__dados.obterValores()

    def obterEstadoJogo(self) -> dict:
        raise NotImplementedError()

    def receber_notificacao_desistencia(self) -> None:
        raise NotImplementedError()

    def receberJogada(self, movimento: dict) -> None:
        raise NotImplementedError()

    def registraAcaoLocal(self, posicao: int) -> None:
        raise NotImplementedError()

    def registrarDados(self) -> None:
        raise NotImplementedError()

    def removerPeca(self, peca: Peca) -> None:
        raise NotImplementedError()

    def removerPecaCemiterio(self) -> None:
        raise NotImplementedError()

    def removerPecaMarcada(self) -> None:
        raise NotImplementedError()

    def removerPecasMarcada(self) -> None:
        raise NotImplementedError()

    def resetar_jogo(self) -> None:
        raise NotImplementedError()

    def statusPartida(self) -> int:
        raise NotImplementedError()
