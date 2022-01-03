class Punct:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return f"{self.__x},{self.__y}"

    @staticmethod
    def distanta_minima_2(punct0, punct1):
        return (punct0.__x - punct1.__x) ** 2 + (punct0.__y - punct1.__y) ** 2

    @staticmethod
    def distanta_minima_3(punct0,punct1,punct2):
        return min(Punct.distanta_minima_2(punct0,punct1),Punct.distanta_minima_2(punct0,punct2), Punct.distanta_minima_2(punct1,punct2))