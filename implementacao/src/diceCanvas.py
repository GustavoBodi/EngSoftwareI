from tkinter import Canvas


class DiceCanvas:
    def __init__(self, canvas: Canvas, x, y) -> None:
        self.__canvas: Canvas = canvas
        self.__text = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.__item = self.__canvas.create_text(x, y, text=self.__text[0], fill="black", font=('Helvetica 60 bold'))

    def atualizarDado(self, dado: int, duplicado: bool) -> None:
        texto = self.__text[dado-1]
        if duplicado:
            texto += texto

        self.__canvas.itemconfig(self.__item, text=texto)
