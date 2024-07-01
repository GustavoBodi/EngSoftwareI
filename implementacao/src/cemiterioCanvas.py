from tkinter import Canvas

class CemiterioCanvas:
    def __init__(self,
                canvas: Canvas,
                 padding_x: int,
                 padding_y: int,
                 base: int,
                 height: int,
                 ):
        self.__canvas = canvas
        self.__padding_x = padding_x
        self.__padding_y = padding_y
        self.__base = base
        self.__height = height
        self.__checkers = []
        self.__reverse = False
        self.draw()

        self.__offset: int = 0

    def draw(self, color: str = "white"):
        x = self.__padding_x
        y = self.__padding_y
        size = self.__height
        x1 = x
        y1 = y
        x2 = x + self.__base
        y2 = y
        x3 = x + self.__base / 2
        y3 = y - size
        points = [x1, y1, x2, y2]
        self.__canvas.create_rectangle(points, fill=color)

    def draw_reverse(self, color: str = "red"):
        x = self.__padding_x
        y = self.__padding_y
        size = self.__height
        x1 = x
        y1 = y
        x2 = x + self.__base
        y2 = y
        x3 = x + self.__base / 2
        y3 = y - size
        points = [x1, y1, x2, y2]
        self.__canvas.create_rectangle(points, fill=color)
        self.__reverse = True

    def remove_checker(self):
        if self.__checkers:
            checker = self.__checkers.pop()
            self.__canvas.delete(checker)
            self.update()

    def get_checker_position(self):
        return self.offset(self.__offset)

    def offset(self, index):
        x = self.__padding_x + self.__base / 2
        y = self.__padding_y - index * (self.__height / 10 + 5)
        return x, y

    def update(self):
        self.__canvas.create_text(self.__x + self.__width / 2,
                                  self.__y + self.__height / 2,
                                  text=str(self.__checkers),
                                  fill="black",
                                  font=('Helvetica 15 bold'))

    def limparOffset(self) -> None:
        self.__offset: int = 0

    def obterOffset(self) -> int:
        return self.__offset

    def aumentarOffset(self) -> None:
        self.__offset += 1

    def reverse(self) -> bool:
        return self.__reverse
