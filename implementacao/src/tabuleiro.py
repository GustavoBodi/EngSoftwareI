from cemiterio import Cemiterio
from dado import Dado
from jogador import Jogador
from linhaTabuleiro import LinhaTabuleiro
from peca import Peca

class Tabuleiro:
    def __init__(self) -> None:
        self.__partidaEmAndamento: bool = False
        self.__cemiterioBrancas: Cemiterio = Cemiterio()
        self.__cemiterioVermelhas: Cemiterio = Cemiterio()
        self.__linhaTabuleiro: LinhaTabuleiro = LinhaTabuleiro()
        self.__pecas: list[Peca] = []
        self.__estadoPartida: int = 0
        self.__dados: Dado = Dado()
        self.__match_status: int = 0

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
        raise NotImplementedError()

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
        raise NotImplementedError()

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
