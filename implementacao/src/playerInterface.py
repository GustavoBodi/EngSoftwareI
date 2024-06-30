from tkinter import Tk, Canvas, Menu, messagebox, simpledialog, Button

from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface

from diceCanvas import DiceCanvas
from cemiterioCanvas import CemiterioCanvas
from posicaoCanvas import PosicaoCanvas
from pecasCanvas import PecasCanvas
from tabuleiro import Tabuleiro
from peca import Peca


class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        self.__tk = Tk()
        self.__tk.title("Gamão")
        self.__width = 1500
        self.__full_width = self.__width + 400
        self.__height = 900
        self.__padding = 50
        self.__thickness = 20
        self.__middle_line_thickness = 20 + self.__thickness
        self.__tk.geometry(f"{self.__full_width}x{self.__height}")
        self.__tk.resizable(True, True)
        self.__background_color = "#39573f"
        self.__color_green = "#45fc03"
        self.__white_color = "#FFFDFA"
        self.__board_background_color = "#efe3af"
        self.__red_color = "#E92019"
        self.__color_yellow = "#FFC90D"
        self.__color_orange = "#FF7F26"
        self.__board_border_color = "#6b0105"
        self.__canvas = Canvas(self.__tk,
                               width=self.__full_width,
                               height=self.__height,
                               bg=self.__background_color)
        self.__triangle_base = self.calculate_triangle_width()
        self.__checker_size = min(self.__triangle_base * 0.42,
                                  self.calculate_triangle_height() * 0.2)
        self.__posicoes: list[PosicaoCanvas] = []
        self.__pecas: list[PecasCanvas] = [PecasCanvas(self.__canvas, self.__checker_size) for _ in range(30)]
        self.__checker_points_box_size = 100
        self.__dice_distance = 50
        self.__cemiterio_brancas = CemiterioCanvas(self.__canvas,
                                           self.__width - self.__padding,
                                           self.__padding + self.__checker_points_box_size + 10,
                                           self.__checker_points_box_size,
                                           self.__checker_points_box_size)

        self.__cemiterio_vermelhas = CemiterioCanvas(self.__canvas,
                                             self.__width - self.__padding,
                                             self.__height - self.__padding -
                                             self.__checker_points_box_size -
                                             self.__thickness / 4 - 10 -
                                             self.__checker_points_box_size,
                                             self.__checker_points_box_size,
                                             self.__checker_points_box_size)

        self.__checker_between_padding = self.__checker_size * 0.8
        self.__checker_bottom_padding = self.__checker_size * 0.3
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
        self.__primeiro_dado = DiceCanvas(self.__canvas,
                                       self.__width + self.__checker_points_box_size +
                                       self.__dice_distance,
                                       self.__height / 2)
        self.__segundo_dado = DiceCanvas(self.__canvas,
                                        self.__width + self.__checker_points_box_size * 2 +
                                        self.__dice_distance,
                                        self.__height / 2)

        self.__dado_label = Button(self.__tk, text="Jogue os dados", command=self.command_dice)
        self.__dado_label.pack()
        self.__canvas.bind("<Button-1>", self.print_checker)
        self.__last_clicked = None

        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.dog_actor = DogActor()
        messagebox.showinfo(message=self.dog_actor.initialize(player_name, self))

        self.__tabuleiro = Tabuleiro(self)
        self.montarTabuleiro()
        estado = self.__tabuleiro.obterEstadoJogo()
        self.atualizarInterface(estado)

        self.__canvas.pack()

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
        self.__menu = Menu(self.__tk)
        filemenu = Menu(self.__menu, tearoff=0)
        filemenu.add_command(label="Iniciar jogo",
                             command=self.iniciar_jogo)
        filemenu.add_command(label="Restaurar estado inicial",
                             command=self.apagar_canvas)
        self.__menu.add_cascade(label="Menu", menu=filemenu)
        self.__tk.config(menu=self.__menu)

    def restaurar_estado_inicial(self):
        print("Restaurar estado inicial não faz nada")

    def iniciar_jogo(self):
        print("Iniciar jogo não faz nada")

    def command_dice(self):
        print("Jogar dados")

    def draw_checkers_initial(self):
        first_triangle_white = self.__posicoes[0]
        second_triangle_white = self.__posicoes[11]
        third_triangle_white = self.__posicoes[16]
        fourth_triangle_white = self.__posicoes[18]

        first_triangle_red = self.__posicoes[23]
        second_triangle_red = self.__posicoes[12]
        third_triangle_red = self.__posicoes[7]
        fourth_triangle_red = self.__posicoes[5]

        for _ in range(2):
            self.draw_checker(first_triangle_white, self.__white_color)
            self.draw_checker(first_triangle_red, self.__red_color)

        for _ in range(3):
            self.draw_checker(third_triangle_white, self.__white_color)
            self.draw_checker(third_triangle_red, self.__red_color)

        for _ in range(5):
            self.draw_checker(second_triangle_white, self.__white_color)
            self.draw_checker(second_triangle_red, self.__red_color)
            self.draw_checker(fourth_triangle_white, self.__white_color)
            self.draw_checker(fourth_triangle_red, self.__red_color)

        # for checker in self.__pecas:
        #     checker.draw()

    def draw_checker(self, triangle: PosicaoCanvas, color: str):
        (x, y) = triangle.get_checker_position()
        # new_checker = PecasCanvas(self.__canvas, x, y,
        #                              self.__checker_size,
        #                              color)
        # triangle.add_checker(new_checker)
        # self.__pecas.append(new_checker)

    def draw_triangle(self, padding_x, padding_y):
        self.__posicoes.append(
                PosicaoCanvas(self.__canvas,
                               padding_x,
                               padding_y,
                               self.__triangle_base,
                               self.calculate_triangle_height(),
                               self.__checker_bottom_padding,
                               self.__checker_between_padding)
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
                self.__posicoes[i].draw(color)
            else:
                self.__posicoes[i].draw_reverse(color)

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
        for _ in range(6):
            padding_x -= self.__triangle_base
            self.draw_triangle(padding_x, padding_y)

    def draw_triagles_left_bottom(self):
        padding_x = self.__padding + self.__thickness + \
                    self.__triangle_base * 6
        padding_y = self.__height - self.__padding - self.__thickness
        for _ in range(6):
            padding_x -= self.__triangle_base
            self.draw_triangle(padding_x, padding_y)

    def draw_triangles_left_top(self):
        padding_x = self.__padding + self.__thickness
        padding_y = self.__padding + self.__thickness
        for _ in range(6):
            self.draw_triangle(padding_x, padding_y)
            padding_x += self.__triangle_base

    def draw_triangles_right_top(self):
        padding_x = self.__width - self.__padding - self.__thickness - \
                    self.__triangle_base * 6
        padding_y = self.__padding + self.__thickness
        for _ in range(6):
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

    def add_checker_to_cemiterio(self, color: str):
        if color == "white":
            self.__cemiterio_brancas.add_checker(color)
        elif color == "red":
            self.__cemiterio_vermelhas.add_checker(color)

    def calculate_triangle_width(self):
        space = self.__width \
                - 2 * self.__padding \
                - 2 * self.__thickness - self.__middle_line_thickness
        return space / 12

    def calculate_triangle_height(self) -> int:
        return (self.__height - 2 * self.__padding - 2 * self.__thickness) \
                * 0.35

    def calculate_checkers_position(self, triangle: PosicaoCanvas):
        (x, y) = triangle.get_checker_position()
        y -= 20
        return (x, y)

    def apagar_canvas(self):
        self.__canvas.delete("all")
        self.__posicoes.clear()
        self.__pecas.clear()

        self.__cemiterio_brancas = CemiterioCanvas(self.__canvas,
                                                   self.__width - self.__padding,
                                                   self.__padding + self.__checker_points_box_size + 10,
                                                   self.__checker_points_box_size,
                                                   self.__checker_points_box_size)

        self.__cemiterio_vermelhas = CemiterioCanvas(self.__canvas,
                                                     self.__width - self.__padding,
                                                     self.__height - self.__padding -
                                                     self.__checker_points_box_size -
                                                     self.__thickness / 4 - 10 -
                                                     self.__checker_points_box_size,
                                                     self.__checker_points_box_size,
                                                     self.__checker_points_box_size)

        self.draw_board_background()
        self.draw_board_border()
        self.draw_triangles()
        self.draw_checkers_initial()
        self.draw_checker_box(self.__width - self.__padding,
                              self.__padding, self.__checker_points_box_size,
                              self.__checker_points_box_size)
        self.draw_checker_box(self.__width - self.__padding,
                              self.__height - self.__padding -
                              self.__checker_points_box_size -
                              self.__thickness / 4,
                              self.__checker_points_box_size,
                              self.__checker_points_box_size)

        self.__primeiro_dado = DiceCanvas(self.__canvas,
                                          self.__width + self.__checker_points_box_size +
                                          self.__dice_distance,
                                          self.__height / 2)
        self.__segundo_dado = DiceCanvas(self.__canvas,
                                         self.__width + self.__checker_points_box_size * 2 +
                                         self.__dice_distance,
                                         self.__height / 2)

        print("tabuleiro resetado")

    def mainloop(self):
        self.__tk.mainloop()

    def receive_start(self, start_status):
        messagebox.showinfo(message=start_status.get_message())

    def atualizarDados(self, dados: list[int]) -> None:
        duplicado = len(dados) > 2
        if not duplicado:
            self.__primeiro_dado.atualizarDado(dados[0], duplicado)
            self.__segundo_dado.atualizarDado(dados[1], duplicado)
        else:
            self.__primeiro_dado.atualizarDado(dados[0], duplicado)
            self.__segundo_dado.atualizarDado(dados[0], duplicado)

    def atualizarInterface(self, estado: dict[str, list[tuple[Peca, int]]]) -> None:
        for posicao in self.__posicoes:
            posicao.limparOffset()

        # self.__cemiterio_vermelhas.limparOffset()
        # self.__cemiterio_brancas.limparOffset()

        print(estado)
        print(self.__pecas)
        for (peca, pecaCanvas) in zip(estado["pecas"], self.__pecas):
            print(peca, pecaCanvas)
            pecaCanvas.apagarCanvas()
            if peca[1] == 24:
                continue

            pecaCanvas.desenhar(peca[0], self.__posicoes[peca[1]])

    def montarTabuleiro(self) -> None:
        self.__tabuleiro.montarTabuleiro()

    def interagirCanvas(self) -> None:
        matchStatus = self.__tabuleiro.statusPartida()
        if matchStatus == 3 or matchStatus == 4:
            movimentoOcorrendo = self.__tabuleiro.movimentoOcorrendo()
            if not movimentoOcorrendo:
                #TODO: selecionar peca
                pass
            else:
                #TODO: selecionar destino
                pass

            estado = self.__tabuleiro.obterEstadoJogo()
            self.atualizarInterface(estado)
