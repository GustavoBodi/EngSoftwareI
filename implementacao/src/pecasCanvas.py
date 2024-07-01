from tkinter import Canvas

from posicaoCanvas import PosicaoCanvas
from cemiterioCanvas import CemiterioCanvas


class PecasCanvas:
    def __init__(self, canvas: Canvas, size: float):
        self.__canvas: Canvas = canvas
        self.__oval: int = 0
        self.__size: float = size

    # def draw(self):
    #     x = self.__padding_x
    #     y = self.__padding_y
    #     self.__canvas.create_oval(x - self.__size / 2,
    #                              float(y),
    #                              x + self.__size / 2,
    #                              float(y + self.__size),
    #                              fill=self.__color,
    #                              outline="",
    #                              tags="checkers")

    def apagarCanvas(self) -> None:
        self.__canvas.delete(self.__oval)

    def desenhar(self, cor: int, posicao: PosicaoCanvas) -> None:
        (x, y) = posicao.get_checker_position()

        offset = -self.__size*0.8*posicao.obterOffset()
        if posicao.reverse():
            offset = -offset

        corReal = "#FFFDFA"
        if cor == 1:
            corReal = "#E92019"

        self.__oval = self.__canvas.create_oval(x - self.__size/2,
                                 y + offset,
                                 x + self.__size/2,
                                 y + self.__size + offset,
                                 fill=corReal,
                                 outline="",
                                 tags=str(posicao.posicao()))

        posicao.aumentarOffset()

    def desenharCemiterio(self, cor: int, cemiterio: CemiterioCanvas) -> None:
        (x, y) = cemiterio.get_checker_position()
        x -= self.__size*16 + self.__size/4

        offset = -self.__size*0.8*cemiterio.obterOffset()
        if cor == 0:
            offset = self.__size*1.6*cemiterio.obterOffset()
            y -= self.__size*2
        else:
            y += self.__size*3

        corReal = "#FFFDFA"
        if cor == 1:
            corReal = "#E92019"

        self.__oval = self.__canvas.create_oval(x - self.__size/2,
                                 y + offset,
                                 x + self.__size/2,
                                 y + self.__size + offset,
                                 fill=corReal,
                                 outline="",
                                 tags=str(25))

        cemiterio.aumentarOffset()
