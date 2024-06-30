from tkinter import Canvas

class PosicaoCanvas:
    def __init__(self,
                 canvas: Canvas,
                 padding_x: int,
                 padding_y: int,
                 base: int,
                 height: int,
                 checkers_bottom_padding: int,
                 checkers_between_padding: int):
        self._padding_x = padding_x
        self._padding_y = padding_y
        self.__base = base
        self.__height = height
        self._canvas = canvas
        self.__checkers_in = 0
        self.__checker_between_padding = checkers_between_padding
        self.__checker_bottom_padding = checkers_bottom_padding
        self.__checkers = []
        self.__reverse = False

        self.__offset: int = 0

    def draw(self, color: str):
        x = self._padding_x
        y = self._padding_y
        size = self.__height
        x1 = x
        y1 = y
        x2 = x + self.__base
        y2 = y
        x3 = x + self.__base / 2
        y3 = y - size
        points = [x1, y1, x2, y2, x3, y3]
        self._canvas.create_polygon(points, fill=color)

    def draw_reverse(self, color: str):
        x = self._padding_x
        y = self._padding_y
        size = self.__height
        x1 = x
        y1 = y
        x2 = x + self.__base
        y2 = y
        x3 = x + self.__base / 2
        y3 = y + size
        points = [x1, y1, x2, y2, x3, y3]
        self._canvas.create_polygon(points, fill=color)
        self.__reverse = True

    def add_checker(self, checker):
        self.__checkers_in += 1
        self.__checkers.append(checker)

    def remove_checker(self, checker):
        self.__checkers_in -= 1
        self.__checkers.remove(checker)

    def get_checker_position(self):
        if (not self.__reverse):
            return (self._padding_x + self.__base / 2,
                    self._padding_y -
                    self.__base / 2 -
                    self.__checker_bottom_padding -
                    self.__checker_between_padding *
                    self.__checkers_in)
        else:
            return (self._padding_x + self.__base / 2,
                    self._padding_y +
                    self.__checker_bottom_padding +
                    self.__checker_between_padding *
                    self.__checkers_in)

    def limparOffset(self) -> None:
        self.__offset: int = 0

    def obterOffset(self) -> int:
        return self.__offset

    def aumentarOffset(self) -> None:
        self.__offset += 1
