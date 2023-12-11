import doctest


class Cat:
    def __init__(self, name: str, colour: str, age: int):
        """
        Создание и подготовка к работе объекта "Кошка"

        :param name: Имя кошки
        :param colour: Цвет кошки
        :param age: Возраст кошки

        Примеры:
        >>> cat = Cat("Мурка","белый",5)  # инициализация экземпляра класса
        """

        if not isinstance(age, int):
            raise TypeError("Возраст кошки должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст кошки должен быть положительным числом")
        self.age = age

        if not isinstance(colour, str):
            raise TypeError("Цвет кошки должен быть типа str")
        self.colour = colour

        if not isinstance(name, str):
            raise TypeError("Имя кошки должно быть типа str")
        self.name = name

    def say_meow(self) -> str:
        """
        Функция воспроизводит мяуканье кошки

        :return: Имя_кошки(name) сказала мяу

        Примеры:
        >>> cat = Cat("Мурка","белый",5)
        >>> cat.say_meow()
        """
        ...

    def human_age(self) -> int:
        """
        Функция, которая определяет,сколько кошеке лет в пересчёте на человечесий возраст

        :return: Человеческий возраст эквивалентный возрасту кошки

        Примеры:
        >>> cat = Cat("Мурка","белый",5)
        >>> cat.human_age()
        """

        ...

    def colour_match(self, kitten_colour: str) -> bool:
        """
        Функция, определяющая совпадает ли цвет кошки с цветом её котёнка
        :param kitten_colour: Цвет котёнка

        :return: Совпадает ли цвет кошки с цветом её котёнка

        Примеры:
        >>> cat = Cat("Мурка","белый",5)
        >>> cat.colour_match("серый")
        """
        if not isinstance(kitten_colour, str):
            raise TypeError("Цвет котёнка должен быть типа str")
        self.kitten_colour = kitten_colour
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
