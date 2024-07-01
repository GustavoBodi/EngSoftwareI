from dado import Dado
from jogador import Jogador
from linhaTabuleiro import LinhaTabuleiro
from peca import Peca


class Tabuleiro:
    def __init__(self, playerInterface) -> None:
        self.__linhaTabuleiro: LinhaTabuleiro = LinhaTabuleiro()
        self.__pecas: list[Peca] = [Peca(0) for _ in range(15)]
        for _ in range(15):
            self.__pecas.append(Peca(1))
        self.__estadoPartida: int = 1
        self.__dados: Dado = Dado(playerInterface)

        self.__jogadorLocal: Jogador = Jogador("", 0, "0")
        self.__jogadorRemoto: Jogador = Jogador("", 1, "1")
        self.__jogadorTurno: Jogador = self.__jogadorLocal
        self.__playerInterface = playerInterface

        self.__partidaEmAndamento: bool = False
        self.__movimentoVazio: bool = True
        self.__movimentoRegular: bool = False
        self.__turnoPossivel: bool = False
        self.__movimentoOcorrendo: bool = False
        self.__esperando: bool = False
        self.__pecaSelecionada: int = 0

    def __inicializar(self, simbolo: int, id: str, nome: str, cor: int) -> None:
        self.__jogadorLocal = Jogador(nome,
                                      cor,
                                      id)

    def adicionarPecas(self, pecas: list[Peca]) -> None:
        for peca in pecas:
            self.__pecas.append(peca)

    def adicionarPeca(self, peca: Peca, posicao: int) -> None:
        self.__linhaTabuleiro.adicionarPeca(peca, posicao)

    def alcancavelDados(self, peca: int, posicao: int, dado: int) -> bool:
        return peca + dado == posicao or peca - dado == posicao

    def avaliarMovimentoSelecionada(self, posicao: int, dado: int) -> tuple[bool, int]:
        return self.avaliarMovimento(self.__pecaSelecionada, posicao, dado)

    def avaliarMovimento(self, peca: int, posicao: int, dado: int) -> tuple[bool, int]:
        if peca == posicao:
            return (True, 3)

        jogador: Jogador = self.identificaJogadorTurno()
        alcancavel: bool = self.alcancavelDados(peca, posicao, dado)
        if alcancavel:
            sentido: bool = self.__linhaTabuleiro.sentidoPontuacao(peca, posicao, jogador)
            if sentido:
                pecas: int = self.__linhaTabuleiro.pecasJogador(posicao, jogador.obterCorAdversario())
                if pecas == 1:
                    removida = self.__linhaTabuleiro.obterPecasPosicao(posicao)[0]
                    self.__linhaTabuleiro.marcarRemovida(removida)
                    self.colocaMovimentoRegular()
                    return (True, 1)
                elif pecas == 0:
                    if posicao == 24:
                        podeSair = self.__linhaTabuleiro.podeSair(jogador.obterCor())
                        if podeSair:
                            self.colocaMovimentoRegular()
                            return (True, 0)
                        else:
                            self.colocaMovimentoIrregular()
                            return (False, 0)
                    else:
                        self.colocaMovimentoRegular()
                        return (True, 2)
                else:
                    self.colocaMovimentoIrregular()
            self.colocaMovimentoIrregular()
            return (False, 0)

        self.colocaMovimentoIrregular()
        return (False, 0)

    def avaliarTermino(self) -> bool:
        jogador = self.identificaJogadorTurno()
        termino = jogador.acabaramPecas()
        if termino:
            self.marcarJogoTerminado()
            jogador.habilitarComoVencedor()

        return termino

    def colocaMovimentoIrregular(self) -> None:
        self.__movimentoRegular = False

    def posicaoJogador(self, posicao: int, jogador: Jogador) -> bool:
        pecas = self.__linhaTabuleiro.obterPecasPosicao(posicao)
        if len(pecas) > 0:
            if pecas[0].cor() == jogador.obterCor():
                return True
            return False
        else:
            return False

    def avaliarPossibilidadeTurno(self) -> bool:
        dados = self.obterDados()

        for dado in dados:
            for peca in self.__pecas:
                for posicao in range(0, 25):
                    (movimentoPossivel, _) = self.avaliarMovimento(self.__linhaTabuleiro.obterPosicao(peca), posicao, dado)
                    if movimentoPossivel:
                        self.__jogadorLocal.marcarMovimentoPossivel()
                        return True

        self.__jogadorLocal.marcarMovimentoImpossivel()
        return False

    def colocaMovimentoOcorrendo(self) -> None:
        self.__movimentoOcorrendo = True

    def colocaMovimentoNaoOcorrendo(self) -> None:
        self.__movimentoOcorrendo = False

    def colocarEsperando(self) -> None:
        self.__estadoPartida = 5

    def comecar_partida(self, jogadores: list[str], idJogadorLocal: str) -> None:
        raise NotImplementedError()

    def definirMovimento(self) -> None:
        self.__movimentoVazio = False

    def definirMovimentoVazio(self) -> None:
        self.__movimentoVazio = True

    def movimentoVazio(self) -> bool:
        return self.__movimentoVazio

    def definirTurnoPossivel(self) -> None:
        self.__turnoPossivel = True

    def definirTerminado(self) -> None:
        self.__partidaEmAndamento = False

    def existePecaCemiterio(self, jogador: Jogador) -> bool:
        jogador_cor = jogador.obterCor()
        if jogador_cor == 0:
            return len(self.__linhaTabuleiro.obterPecasCemiterioBranco()) > 0
        else:
            return len(self.__linhaTabuleiro.obterPecasCemiterioVermelho()) > 0

    def identificaJogadorTurno(self) -> Jogador:
        return self.__jogadorTurno

    def jogarDados(self) -> None:
        self.__dados.zerarDados()
        valor1 = self.__dados.gerarNumero()
        valor2 = self.__dados.gerarNumero()

        if valor1 == valor2:
            self.__dados.duplicarDados()

        movimentoPossivel = self.avaliarPossibilidadeTurno()

        if movimentoPossivel:
            self.__jogadorLocal.definirTurnoPossivel()
            valores = self.__dados.obterValores()
            self.__playerInterface.atualizarDados(valores)
        else:
            self.__jogadorLocal.definirTurnoTerminado()

    def montarTabuleiro(self) -> None:
        self.limparTabuleiro()
        for (quantidade, posicao) in [(5,5), (3,7), (5,12), (2,23)]:
            pecas = self.__linhaTabuleiro.posicionaPecas(self.__jogadorLocal, posicao, quantidade)
            pecas += self.__linhaTabuleiro.posicionaPecas(self.__jogadorRemoto, 23-posicao, quantidade)
            self.adicionarPecas(pecas)

    def limparTabuleiro(self) -> None:
        self.__jogadorLocal.limparTabuleiro()
        self.__jogadorRemoto.limparTabuleiro()
        self.__linhaTabuleiro.removerPecas()
        self.removerPecas()

    def marcarJogoTerminado(self) -> None:
        self.__partidaEmAndamento = False

    def jogoTerminado(self) -> bool:
        return self.__partidaEmAndamento

    def movimentoOcorrendo(self) -> bool:
        return self.__movimentoOcorrendo

    def colocaMovimentoRegular(self) -> None:
        self.__movimentoRegular = True

    def obterDados(self) -> list[int]:
        return self.__dados.obterValores()

    def removerDado(self, valor: int) -> None:
        return self.__dados.removerDado(valor)

    def obterEstadoJogo(self) -> dict:
        estado = {}
        listaPecasPosicoes = []
        for i, posicao in enumerate(self.__linhaTabuleiro.obterPosicoes()):
            for ocupante in posicao.obterOcupantes():
                listaPecasPosicoes.append((ocupante.cor(), i))
        for peca in self.__linhaTabuleiro.obterPecasCemiterioVermelho():
            listaPecasPosicoes.append((peca.cor(), 25))
        for peca in self.__linhaTabuleiro.obterPecasCemiterioBranco():
            listaPecasPosicoes.append((peca.cor(), 25))
        for peca in self.__linhaTabuleiro.obterPecasRemovidas():
            listaPecasPosicoes.append((peca.cor(), 24))
        estado['pecas'] = listaPecasPosicoes
        return estado

    def receber_notificacao_desistencia(self) -> None:
        raise NotImplementedError()

    def receberJogada(self, movimento: dict) -> None:
        for (peca, pos_final) in movimento['posicoes']:
            self.__linhaTabuleiro.moverPeca(peca, pos_final)
        for peca in movimento['fora_tabuleiro']:
            self.__linhaTabuleiro.removerPeca(peca)
        for (peca, cemiterio) in movimento['mortas']:
            self.__linhaTabuleiro.matarPeca(peca)

    def registraAcaoLocal(self, posicao: int) -> None:
        self.__pecaSelecionada = posicao

    def matarPecaMarcada(self) -> None:
        self.__linhaTabuleiro.matarPecaMarcada()

    def moverPecaSelecionada(self, destino: int) -> None:
        peca = self.__linhaTabuleiro.obterPosicoes()[self.__pecaSelecionada].obterOcupantes()[0]
        self.__linhaTabuleiro.moverPeca(peca, destino)

    def removerPecaSelecionada(self) -> None:
        self.__linhaTabuleiro.removerPecaPosicao(self.__pecaSelecionada)

    def removerPecas(self) -> None:
        self.__pecas.clear()

    def removerPecaMarcada(self) -> None:
        peca = self.__linhaTabuleiro.pecaMarcadaRemovida()
        self.__linhaTabuleiro.matarPeca(peca)

    def resetar_jogo(self) -> None:
        self.__jogadorLocal = Jogador()
        self.__jogadorRemoto = Jogador()
        self.__pecas.clear()

    def statusPartida(self) -> int:
        return self.__estadoPartida

    def definirStatusPartida(self, status: int) -> None:
        self.__estadoPartida = status
