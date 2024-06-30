from cemiterio import Cemiterio
from dado import Dado
from jogador import Jogador
from linhaTabuleiro import LinhaTabuleiro
from peca import Peca
from main import PlayerInterface


class Tabuleiro:
    def __init__(self) -> None:
        self.__linhaTabuleiro: LinhaTabuleiro = LinhaTabuleiro()
        self.__pecas: list[Peca] = [Peca(0) for _ in range(15)]
        for _ in range(15):
            self.__pecas.append(Peca(1))
        self.__estadoPartida: int = 0
        self.__dados: Dado = Dado()
        self.__match_status: int = 0

        self.__jogadorLocal: Jogador
        self.__jogadorRemoto: Jogador
        self.__jogadorTurno: Jogador = None
        self.__playerInterface: PlayerInterface = PlayerInterface()

        self.__partidaEmAndamento: bool = False
        self.__movimento = {}
        self.__movimentoRegular: bool = False
        self.__turnoPossivel: bool = False
        self.__movimentoOcorrendo: bool = False
        self.__esperando: bool = False

    def __inicializar(self, simbolo: int, id: str, nome: str, cor: int) -> None:
        self.__jogadorLocal = Jogador(self, self.__linhaTabuleiro,
                                      self.__dados,
                                      nome,
                                      cor,
                                      id)

    def adicionarPeca(self, peca: Peca, posicao: int) -> None:
        self.__linhaTabuleiro.adicionarPeca(peca, posicao)

    def adicionarPecaForaTabuleiro(self, peca: Peca) -> None:
        self.__linhaTabuleiro.removerPecaTabuleiro(peca)

    def alcancavelDados(self, peca: Peca, posicao: int, dado: int) -> bool:
        for i, posicao in enumerate(self.__linhaTabuleiro.obterPosicoes()):
            for peca_busca in posicao.obterOcupantes():
                if peca == peca_busca:
                    if i + dado == posicao or i - dado == posicao:
                        return True
                    else:
                        return False

    def avaliarMovimento(self, peca: Peca, posicao: int, dado: int) -> bool:
        jogador = self.identificaJogadorTurno()
        alcalcavel = self.alcancavelDados(peca, posicao, dado)
        sentido = jogador.sentidoPontuacao(peca, posicao)
        if alcalcavel and sentido:
            quantidade = self.__linhaTabuleiro.pecasAdversario(posicao, jogador.obterCorAdversario())

            if quantidade == 1:
                self.__linhaTabuleiro.marcarRemovida(peca)
                self.movimentoRegular()
                return True
            elif quantidade == 0:
                if posicao == 24:
                    sairam = self.__linhaTabuleiro.pecasSairam(jogador)
                    if sairam:
                        self.marcarPontoJogador(jogador)
                        self.movimentoRegular()
                        return True
                    else:
                        self.colocaMovimentoIrregular()
                        return False
                else:
                    self.movimentoRegular()
                    return True

        self.colocaMovimentoIrregular()
        return False

    def avaliarTermino(self) -> bool:
        jogador = self.identificaJogadorTurno()
        termino = jogador.acabaramPecas()
        if termino:
            self.marcarTerminado()
            jogador.habilitarComoVencedor()

    def colocaMovimentoIrregular(self) -> None:
        self.__movimentoRegular = False

    def colocaMovimentoOcorrendo(self) -> None:
        self.__movimentoOcorrendo = True

    def colocarEsperando(self) -> None:
        self.__esperando = True

    def comecar_partida(self, jogadores: list[str], idJogadorLocal: str) -> None:
        raise NotImplementedError()

    def definirMovimento(self) -> None:
        self.__movimento.clear()

    def definirTurnoPossivel(self) -> None:
        self.__turnoPossivel = True

    def definirTerminado(self) -> None:
        self.__partidaEmAndamento = False

    def existePecaCemiterio(self, jogador: Jogador) -> bool:
        jogador_cor = jogador.obterCor()
        if jogador_cor == 0:
            return len(self.__linhaTabuleiro.obterPecasCemiterioBranco()) > 0
        elif jogador_cor == 1:
            return len(self.__linhaTabuleiro.obterPecasCemiterioVermelho()) > 0

    def identificaJogadorTurno(self) -> Jogador:
        return self.__jogadorTurno

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
        self.__linhaTabuleiro.removerPecas()

    def marcarJogoTerminado(self) -> None:
        self.__partidaEmAndamento = False

    def marcarMovimento(self, estado: str) -> None:
        self.__movimento['state'] = estado

    def marcarTerminado(self) -> None:
        self.__movimento['state'] = "finished"

    def movimentoOcorrendo(self) -> bool:
        self.__movimentoOcorrendo = True

    def movimentoRegular(self) -> None:
        self.__movimentoRegular = True

    def obterDado(self) -> list[int]:
        return self.__dados.obterValores()

    def obterEstadoJogo(self) -> dict:
        estado = {}
        listaPecasPosicoes = []
        for i, posicao in enumerate(self.__linhaTabuleiro.obterPosicoes()):
            for ocupantes in posicao.obterOcupantes():
                listaPecasPosicoes.append((ocupantes, i))
        for peca in self.__linhaTabuleiro.obterPecasCemiterioVermelho():
            listaPecasPosicoes.append((peca, 25))
        for peca in self.__linhaTabuleiro.obterPecasCemiterioBranco():
            listaPecasPosicoes.append((peca, 25))
        for peca in self.__linhaTabuleiro.obterPecasRemovidas():
            listaPecasPosicoes.append((peca, 24))
        estado['pecas'] = listaPecasPosicoes
        return estado

    def receber_notificacao_desistencia(self) -> None:
        raise NotImplementedError()

    def receberJogada(self, movimento: dict) -> None:
        for (peca, pos_final) in movimento['posicoes']:
            self.__linhaTabuleiro.moverPeca(peca, pos_final)
        for peca in movimento['fora_tabuleiro']:
            self.__linhaTabuleiro.retirarPecaTabuleiro(peca)
        for (peca, cemiterio) in movimento['mortas']:
            self.__linhaTabuleiro.matarPeca(peca)

    def registraAcaoLocal(self, posicao: int) -> None:
        raise NotImplementedError()

    def removerPeca(self, peca: Peca) -> None:
        self.__linhaTabuleiro.removerPeca(peca)

    def removerPecaMarcada(self) -> None:
        peca = self.__linhaTabuleiro.pecaMarcadaRemovida()
        self.__linhaTabuleiro.removerPeca(peca)

    def resetar_jogo(self) -> None:
        self.__jogadorLocal = Jogador()
        self.__jogadorRemoto = Jogador()
        self.__pecas.clear()

    def statusPartida(self) -> int:
        raise NotImplementedError()
