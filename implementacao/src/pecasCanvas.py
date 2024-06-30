from tkinter import Canvas

from posicaoCanvas import PosicaoCanvas
from peca import Peca


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

    def desenhar(self, peca: Peca, posicao: PosicaoCanvas) -> None:
        (x, y) = posicao.get_checker_position()

        offset = -self.__size*0.8*posicao.obterOffset()
        if posicao.reverse():
            offset = -offset

        cor = "#FFFDFA"
        if peca.vermelha():
            cor = "#E92019"

        self.__oval = self.__canvas.create_oval(x - self.__size/2,
                                 y + offset,
                                 x + self.__size/2,
                                 y + self.__size + offset,
                                 fill=cor,
                                 outline="",
                                 tags=str(posicao.posicao()))

        posicao.aumentarOffset()
