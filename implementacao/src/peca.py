class Peca:
    def __init__(self, cor: int) -> None:
        self.__cor: int = cor

    def cor(self) -> int:
        return self.__cor

    def branca(self) -> bool:
        return self.__cor == 0

    def vermelha(self) -> bool:
        return self.__cor == 1
