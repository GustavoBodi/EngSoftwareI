from tkinter import Canvas

class PecasCanvas:
    def __init__(self, canvas: Canvas,
                 padding_x: int,
                 padding_y: int,
                 size: int,
                 color: str):
        self.__padding_x = padding_x
        self.__padding_y = padding_y
        self.__size = size
        self.__canvas = canvas
        self.__color = color

    def draw(self):
        x = self.__padding_x
        y = self.__padding_y
        self.__canvas.create_oval(x - self.__size / 2,
                                 float(y),
                                 x + self.__size / 2,
                                 float(y + self.__size),
                                 fill=self.__color,
                                 outline="",
                                 tags="checkers")

    def apagarCanvas(self) -> None:
        raise NotImplementedError()

    def desenhar(self, posicao: int, offset: int) -> None:
        raise NotImplementedError()
