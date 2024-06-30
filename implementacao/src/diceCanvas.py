class DiceCanvas:
    def __init__(self, canvas, x, y) -> None:
        self.__canvas = canvas
        dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.__canvas.create_text(x, y, text=dice[2], fill="black", font=('Helvetica 60 bold'))

    def atualizarDado(self, dado: int, duplicado: bool) -> None:
        raise NotImplementedError()

    def update(self, valor: list[int]) -> None:
        raise NotImplementedError()
