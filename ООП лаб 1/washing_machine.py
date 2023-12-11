import doctest


class WashingMachine:
    def __init__(self, brand: str, colour: str, drying_mode: bool):
        """
        Создание и подготовка к работе объекта "Стиральная машина"

        :param brand: Бренд стиральной машины
        :param colour: Цвет стиральной машин
        :param drying_mode: Наличие режима сушки

        Примеры:
        >>> washing_machine =WashingMachine ("Bosсh","white",True)  # инициализация экземпляра класса
        """

        if not isinstance(brand, str):
            raise TypeError("Бренд стиральной машины должен быть типа str")
        self.brand = brand

        if not isinstance(colour, str):
            raise TypeError("Цвет стиральной машины должен быть типа str")
        self.colour = colour

        if not isinstance(drying_mode, bool):
            raise TypeError("Наличие режима сушки должно быть типа bool")
        self.drying_mode = drying_mode

    def has_drying_mode(self) -> bool:
        """
        Функция определяет имеется ли у данной стиральной машины режим сушки

        :return: Имеется ли у данной стиральной машины режим сушки

        Примеры:
        >>> washing_machine = WashingMachine ("Bosсh","white",True)
        >>> washing_machine.has_drying_mode()
        """

        ...

    def change_colour(self, new_colour: str) -> None:
        """
        Функция перекрашивает стиральную машину в заданый цвет
        :param new_colour: Новый цвет стиральной машины

        Примеры:
        >>> washing_machine =WashingMachine ("Bosсh","white",True)
        >>> washing_machine.change_colour("серый")
        """
        if not isinstance(new_colour, str):
            raise TypeError("Новый цвет стиральной машины должен быть типа str")


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
