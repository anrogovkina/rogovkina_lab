import doctest


class ChristmasTree:
    def __init__(self, height: float, type: str, lights: bool):
        """
        Создание и подготовка к работе объекта "Ёлка"

        :param height: Высота ёлки
        :param type: Разновидность ёлки
        :param lights: Огоньки на ёлке
        Примеры:
        >>> xmas_tree = ChristmasTree(1.56,"Пихта Нордмана",False)  # инициализация экземпляра класса
        """

        if not isinstance(height, (int, float)):
            raise TypeError("Высота ёлки должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота ёлки должна быть положительным числом")
        self.height = height

        if not isinstance(type, str):
            raise TypeError("Разновидность ёлки должна быть типа str")
        self.type = type

        if not isinstance(lights, bool):
            raise TypeError("Наличие огоньков на ёлке долно быь типа bool")
        self.type = type

    def lights_on(self) -> None:
        """
        Функция включает огоньки на ёлке(изменяет значние аргумента lights, если оно равно False, на True)

        Примеры:
        >>> xmas_tree = ChristmasTree(1.56,"Пихта Нордмана",False)
        >>> xmas_tree.lights_on()
        """

        ...

    def fits_the_room(self, ceiling_height: float) -> bool:
        """
        Функция определяет, поместится ли ёлка в комнате с учётом высоты потолка
        :param ceiling_height: Высота потолка в комнате

        :return: Поместится ли ёлка в комнате с учётом высоты потолка

        Примеры:
        >>> xmas_tree = ChristmasTree(1.56,"Пихта Нордмана",False)
        >>> xmas_tree.fits_the_room(2.00)
        """
        if not isinstance(ceiling_height, (int, float)):
            raise TypeError("Высота потолка должна быть типа int или float")
        if ceiling_height <= 0:
            raise ValueError("Высота потолка должна быть положительным числом")
        self.ceiling_height = ceiling_height
        ...


if __name__ == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации
