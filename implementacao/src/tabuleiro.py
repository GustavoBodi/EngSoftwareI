from tkinter import messagebox

from dado import Dado
from jogador import Jogador
from linhaTabuleiro import LinhaTabuleiro
from peca import Peca


class Tabuleiro:
    def __init__(self, playerInterface) -> None:
        self.__linhaTabuleiro: LinhaTabuleiro = LinhaTabuleiro()
        self.__pecas: list[Peca] = []
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

    def inicializar(self, nome: str, cor: int, id: str, local: bool) -> None:
        if local:
            self.__jogadorLocal = Jogador(nome, cor, id)
        else:
            self.__jogadorRemoto = Jogador(nome, cor, id)

    def adicionarPecas(self, pecas: list[Peca]) -> None:
        for peca in pecas:
            self.__pecas.append(peca)

    def adicionarPeca(self, peca: Peca, posicao: int) -> None:
        self.__linhaTabuleiro.adicionarPeca(peca, posicao)
        self.__pecas.append(peca)

    def alcancavelDados(self, peca: int, posicao: int, dado: int) -> bool:
        if peca == 25:
            if self.__jogadorLocal.obterCor() == 0:
                peca = 24
            else:
                peca = -1

        if posicao == 24:
            return peca + dado >= 24 or peca - dado < 0

        return peca + dado == posicao or peca - dado == posicao

    def avaliarMovimentoSelecionada(self, posicao: int, dado: int) -> tuple[bool, int]:
        return self.avaliarMovimento(self.__pecaSelecionada, posicao, dado)

    def avaliarMovimento(self, peca: int, posicao: int, dado: int) -> tuple[bool, int]:
        if peca == posicao:
            return (True, 3)

        alcancavel: bool = self.alcancavelDados(peca, posicao, dado)
        if alcancavel:
            sentido: bool = self.__linhaTabuleiro.sentidoPontuacao(peca, posicao, self.__jogadorLocal)
            if sentido:
                if posicao == 24:
                    podeSair = self.__linhaTabuleiro.podeSair(self.__jogadorLocal.obterCor())
                    if podeSair:
                        self.colocaMovimentoRegular()
                        return (True, 0)
                    else:
                        self.colocaMovimentoIrregular()
                        return (False, 0)

                pecas: int = self.__linhaTabuleiro.pecasJogador(posicao, self.__jogadorLocal.obterCorAdversario())
                if pecas == 1:
                    removida = self.__linhaTabuleiro.obterPecasPosicao(posicao)[0]
                    self.__linhaTabuleiro.marcarRemovida(removida)
                    self.colocaMovimentoRegular()
                    return (True, 1)
                elif pecas == 0:
                    self.colocaMovimentoRegular()
                    return (True, 2)
                else:
                    self.colocaMovimentoIrregular()
            self.colocaMovimentoIrregular()
            return (False, 0)

        self.colocaMovimentoIrregular()
        return (False, 0)

    def avaliarTermino(self) -> bool:
        quantidade = 0
        for peca in self.__linhaTabuleiro.obterPosicoes()[24].obterOcupantes():
            if peca.cor() == self.__jogadorLocal.obterCor():
                quantidade += 1

        termino = quantidade == 15
        if termino:
            self.marcarJogoTerminado()
            self.__estadoPartida = 2
            self.__jogadorLocal.habilitarComoVencedor()
            messagebox.showinfo(message="Você Venceu")

        return termino

    def colocaMovimentoIrregular(self) -> None:
        self.__movimentoRegular = False

    def posicaoJogador(self, posicao: int, jogador: Jogador) -> bool:
        if posicao == 24:
            return False

        if posicao == 25:
            pecas = []
            if jogador.obterCor() == 0:
                pecas = self.__linhaTabuleiro.obterPecasCemiterioBranco()
            else:
                pecas = self.__linhaTabuleiro.obterPecasCemiterioVermelho()
            return len(pecas) > 0

        pecas = self.__linhaTabuleiro.obterPecasPosicao(posicao)
        return len(pecas) > 0 and pecas[0].cor() == jogador.obterCor()

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

    def jogadorLocal(self) -> Jogador:
        return self.__jogadorLocal

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
        # for (quantidade, posicao) in [(14, 24), (1,0)]:
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
        return not self.__partidaEmAndamento

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
        estado['pecas'] = listaPecasPosicoes
        return estado

    def receber_notificacao_desistencia(self) -> None:
        raise NotImplementedError()

    def receberJogada(self, movimento: dict) -> None:
        self.limparTabuleiro()
        for (cor, posicao) in movimento['pecas']:
            if posicao <= 24:
                if cor == self.__jogadorLocal.obterCor():
                    pecas = self.__linhaTabuleiro.posicionaPecas(self.__jogadorLocal, posicao, 1)
                    self.adicionarPecas(pecas)
                else:
                    pecas = self.__linhaTabuleiro.posicionaPecas(self.__jogadorRemoto, posicao, 1)
                    self.adicionarPecas(pecas)
            if posicao == 25:
                peca = Peca(cor)
                self.__pecas.append(peca)
                self.__linhaTabuleiro.adicionarPecaCemiterio(peca)

        if movimento["match_status"] == "finished":
            self.marcarJogoTerminado()
            self.__estadoPartida = 2
            self.__jogadorRemoto.habilitarComoVencedor()
            messagebox.showinfo(message="Você Perdeu")

    def registraAcaoLocal(self, posicao: int) -> None:
        self.__pecaSelecionada = posicao

    def matarPecaMarcada(self) -> None:
        self.__linhaTabuleiro.matarPecaMarcada()

    def moverPecaSelecionada(self, destino: int) -> None:
        if self.__pecaSelecionada == 25:
            if self.__jogadorLocal.obterCor() == 0:
                peca = self.__linhaTabuleiro.obterPecasCemiterioBranco()[0]
            else:
                peca = self.__linhaTabuleiro.obterPecasCemiterioVermelho()[0]
        else:
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
