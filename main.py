from tkinter import Tk, Canvas, Menu
from tkinter import *
from tkinter.ttk import *


class TriangleCanvas:
    def __init__(self,
                 canvas: Canvas,
                 padding_x: int,
                 padding_y: int,
                 base: int,
                 height: int):
        self._padding_x = padding_x
        self._padding_y = padding_y
        self.__base = base
        self.__height = height
        self._canvas = canvas
        self.__checkers_in = 0
        self.__checker_between_padding = 35
        self.__checker_bottom_padding = 10
        self.__checkers = []
        self.__reverse = False

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


class CheckersCanvas:
    def __init__(self, canvas: Canvas,
                 padding_x: int,
                 padding_y: int,
                 size: int,
                 color: str):
        self._padding_x = padding_x
        self._padding_y = padding_y
        self._size = size
        self._canvas = canvas
        self._color = color

    def draw(self):
        x = self._padding_x
        y = self._padding_y
        self._canvas.create_oval(x - self._size / 2,
                                 y,
                                 x + self._size / 2,
                                 y + self._size,
                                 fill=self._color,
                                 outline="",
                                 tag="checkers")


class PlayerActor:
    def __init__(self):
        self.__tk = Tk()
        self.__tk.title("Gamão")
        self.__width = 1600
        self.__full_width = self.__width + 400
        self.__height = 1000
        self.__padding = 50
        self.__thickness = 20
        self.__middle_line_thickness = 20 + self.__thickness
        self.__tk.geometry(f"{self.__full_width}x{self.__height}")
        self.__tk.resizable(False, False)
        self.__background_color = "#39573f"
        self.__color_green = "#45fc03"
        self.__white_color = "#FFFDFA"
        self.__board_background_color = "#efe3af"
        self.__red_color = "#E92019"
        self.__color_yellow = "#FFC90D"
        self.__color_orange = "#FF7F26"
        self.__board_border_color = "#6b0105"
        self.__canvas = Canvas(self.__tk,
                               width=self.__width,
                               height=self.__height,
                               bg=self.__background_color)
        self.__triangle_canvas: [TriangleCanvas] = []
        self.__checker_canvas: [CheckersCanvas] = []
        self.__triangle_base = self.calculate_triangle_width()
        self.__checker_size = self.__triangle_base * 0.42
        self.__checker_points_box_size = 100
        self.__dice_distance = 50
        self.draw_board_background()
        self.draw_board_border()
        self.draw_triangles()
        self.draw_checkers_initial()
        self.create_menu()
        self.draw_checker_box(self.__width - self.__padding,
                              self.__padding, self.__checker_points_box_size,
                              self.__checker_points_box_size)
        self.draw_checker_box(self.__width - self.__padding,
                              self.__height - self.__padding -
                              self.__checker_points_box_size -
                              self.__thickness / 4,
                              self.__checker_points_box_size,
                              self.__checker_points_box_size)
        self.draw_dice(self.__width + self.__checker_points_box_size +
                       self.__dice_distance,
                       self.__height / 2)
        self.draw_dice(self.__width + self.__checker_points_box_size * 2 +
                       self.__dice_distance,
                       self.__height / 2)
        self.draw_dice_text(self.__width + self.__checker_points_box_size * 2,
                            self.__height / 2 + self.__dice_distance)
        self.__canvas.bind("<Button-1>", self.print_checker)
        self.__last_clicked = None

    def print_checker(self, event):
        self.__canvas = event.widget
        x = self.__canvas.canvasx(event.x)
        y = self.__canvas.canvasy(event.y)

        overlapping = self.__canvas.find_overlapping(x, y, x+1, y+1)
        checkers = self.__canvas.find_withtag("checkers")
        dice_text = set(overlapping) & set(self.__canvas.find_withtag("dicebox"))
        if (len(dice_text) > 0):
            print("Clicou no jogar dados")
        for item in set(overlapping) & set(checkers):
            self.__canvas.itemconfigure(item, outline=self.__color_green)
            if (self.__last_clicked is not None):
                self.__canvas.itemconfigure(self.__last_clicked,
                                            outline="")
            self.__last_clicked = item

    def create_menu(self):
        menubar = Menu(self.__tk)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Iniciar jogo",
                             command=self.iniciar_jogo)
        filemenu.add_command(label="Restaurar estado inicial",
                             command=self.restaurar_estado_inicial)
        menubar.add_cascade(label="Menu", menu=filemenu)
        self.__tk.config(menu=menubar)

    def restaurar_estado_inicial(self):
        print("Restaurar estado inicial não faz nada")

    def iniciar_jogo(self):
        print("Iniciar jogo não faz nada")

    def draw_dice(self, x, y):
        dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.__canvas.create_text(x, y, text=dice[2],
                                  fill="black",
                                  font=('Helvetica 60 bold'))

    def draw_dice_text(self, x, y):
        self.__canvas.create_text(x, y, text="Jogue os dados",
                                  fill="black",
                                  font=('Helvetica 20 bold'),
                                  tag="dicebox")

    def draw_checkers_initial(self):
        first_triangle_white = self.__triangle_canvas[0]
        second_triangle_white = self.__triangle_canvas[11]
        third_triangle_white = self.__triangle_canvas[16]
        fourth_triangle_white = self.__triangle_canvas[18]

        first_triangle_red = self.__triangle_canvas[23]
        second_triangle_red = self.__triangle_canvas[12]
        third_triangle_red = self.__triangle_canvas[7]
        fourth_triangle_red = self.__triangle_canvas[5]

        for i in range(2):
            self.draw_checker(first_triangle_white, self.__white_color)
            self.draw_checker(first_triangle_red, self.__red_color)

        for i in range(3):
            self.draw_checker(third_triangle_white, self.__white_color)
            self.draw_checker(third_triangle_red, self.__red_color)

        for i in range(5):
            self.draw_checker(second_triangle_white, self.__white_color)
            self.draw_checker(second_triangle_red, self.__red_color)
            self.draw_checker(fourth_triangle_white, self.__white_color)
            self.draw_checker(fourth_triangle_red, self.__red_color)

        for checker in self.__checker_canvas:
            checker.draw()

    def draw_checker(self, triangle: TriangleCanvas, color: str):
        (x, y) = triangle.get_checker_position()
        new_checker = CheckersCanvas(self.__canvas, x, y,
                                     self.__checker_size,
                                     color)
        triangle.add_checker(new_checker)
        self.__checker_canvas.append(new_checker)

    def draw_triangle(self, padding_x, padding_y):
        self.__triangle_canvas.append(
                TriangleCanvas(self.__canvas,
                               padding_x,
                               padding_y,
                               self.__triangle_base,
                               self.calculate_triangle_height())
                )

    def draw_triangles(self):
        self.draw_triagles_right_bottom()
        self.draw_triagles_left_bottom()
        self.draw_triangles_left_top()
        self.draw_triangles_right_top()
        color = self.__color_orange
        for i in range(24):
            if (i % 2 == 0):
                color = self.__color_yellow
            else:
                color = self.__color_orange
            if (i < 12):
                self.__triangle_canvas[i].draw(color)
            else:
                self.__triangle_canvas[i].draw_reverse(color)

    def draw_checker_box(self, x, y, w, h):
        thickness = self.__thickness / 2
        self.__canvas.create_rectangle(x + thickness / 2, y + thickness / 2, x + w, y + h,
                                       outline=self.__board_border_color,
                                       width=thickness,
                                       fill=self.__board_background_color)
        self.__canvas.create_text(x + thickness / 4 + w / 2, y + h / 2 + thickness / 4, text="0",
                                  fill="black",
                                  font=('Helvetica 15 bold'))

    def draw_triagles_right_bottom(self):
        padding_x = self.__width - self.__padding - self.__thickness
        padding_y = self.__height - self.__padding - self.__thickness
        for i in range(6):
            padding_x -= self.__triangle_base
            self.draw_triangle(padding_x, padding_y)

    def draw_triagles_left_bottom(self):
        padding_x = self.__padding + self.__thickness + \
                    self.__triangle_base * 6
        padding_y = self.__height - self.__padding - self.__thickness
        for i in range(6):
            padding_x -= self.__triangle_base
            self.draw_triangle(padding_x, padding_y)

    def draw_triangles_left_top(self):
        padding_x = self.__padding + self.__thickness
        padding_y = self.__padding + self.__thickness
        for i in range(6):
            self.draw_triangle(padding_x, padding_y)
            padding_x += self.__triangle_base

    def draw_triangles_right_top(self):
        padding_x = self.__width - self.__padding - self.__thickness - \
                    self.__triangle_base * 6
        padding_y = self.__padding + self.__thickness
        for i in range(6):
            self.draw_triangle(padding_x, padding_y)
            padding_x += self.__triangle_base

    def draw_board_border(self):
        self.__canvas.create_rectangle(self.__padding,
                                       self.__padding,
                                       self.__width - self.__padding,
                                       self.__thickness + self.__padding,
                                       width=0, fill=self.__board_border_color)
        self.__canvas.create_rectangle(self.__padding,
                                       self.__height - self.__padding,
                                       self.__width - self.__padding,
                                       self.__height - self.__padding
                                       - self.__thickness,
                                       width=0, fill=self.__board_border_color)
        self.__canvas.create_rectangle(self.__padding,
                                       self.__padding,
                                       self.__padding + self.__thickness,
                                       self.__height - self.__padding,
                                       width=0, fill=self.__board_border_color)
        self.__canvas.create_rectangle(self.__width - self.__padding
                                       - self.__thickness,
                                       self.__padding,
                                       self.__width - self.__padding,
                                       self.__height - self.__padding,
                                       width=0, fill=self.__board_border_color)
        self.__canvas.create_line(self.__width / 2,
                                  self.__padding,
                                  self.__width / 2,
                                  self.__height - self.__padding,
                                  width=self.__middle_line_thickness,
                                  fill=self.__board_border_color)

    def draw_board_background(self):
        padding = 50
        self.__canvas.create_rectangle(padding,
                                       padding,
                                       self.__width - padding,
                                       self.__height - padding,
                                       fill=self.__board_background_color)

    def create(self):
        self.__canvas.pack(fill=BOTH, expand=True)

    def calculate_triangle_width(self):
        space = self.__width \
                - 2 * self.__padding \
                - 2 * self.__thickness - self.__middle_line_thickness
        return space / 12

    def calculate_triangle_height(self) -> int:
        return (self.__height - 2 * self.__padding - 2 * self.__thickness) \
                * 0.35

    def calculate_checkers_position(self, triangle: TriangleCanvas):
        (x, y) = triangle.get_checker_position()
        y -= 20
        return (x, y)

    def mainloop(self):
        self.__tk.mainloop()


if __name__ == "__main__":
    player = PlayerActor()
    player.create()
    player.mainloop()
