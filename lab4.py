
class PC:
    """
    Документация на класс.
    Класс описывает модель компьютера
    """

    def __init__(self, os: str, price: int):
        """
        Создание объекта "персональный компьютер"(базовый класс)

        :param os: Операционная система компьютера
        :param price: Цена компьютера(руб)
        """
        self.os = os
        self.price = price

    def install_app(self, app: str) -> None:
        """
        Метод, устанавливающий приложение на компьютер

        :param app: приложение, устанавливаемое на компьютер
        """
        ...

    def is_pc_on(self) -> bool:
        """
        Функция, проверяющая, вкулючен ли компьютер
        :return: Включён ли ноутбук
        """
        ...

    def __str__(self) -> str:
        """
        Метод __str__ должен возвращать строку, где "оперционная система" берется с помощью атрибута os,
        "цена" берется с помощью атрибута price
        :return: Персональный компьютер. Операционная система: операционная система. Цена: цена.
        """
        return f"Персональный компьютер. Операционная система: {self.os}. Цена: {self.price}."

    def __repr__(self):
        """
        Метод __repr__ должен возвращать валидную python строку,
        по которой можно инициализировать точно такой же экземпляр
        :return: PC(os=_, price=_)
        """
        return f"{self.__class__.__name__}(os={self.os}, price={self.price})"


if __name__ == "__main__":

    class Laptop(PC):
        """
        Документация на класс.
        Класс описывает модель ноутбука
        """

        def __init__(self, os: str, price: int, screen_size: int):

            """
            Создание и подготовка к работе объекта "MacBook" (дочерний класс)

            :param os: Операционная система
            :param price: Цена ноутбука(руб)
            :param screen_size: Диагональ экрана ноутбука
            """

            super().__init__(price)
            # Атрибут price наследуется из базового класса
            self.screen_size = screen_size
            self.os = os

        def install_app(self, app: str) -> None:

            """
            Метод для установки приложения необходимо перегрузить(так как в зависимости
            от ОС меняются допустимые приложения)
            :param app: приложение, устанавливаемое на ноутбук
            """
            ...

        def __repr__(self) -> str:
            """
            Метод __repr__ должен возвращать валидную python строку,
            по которой можно инициализировать точно такой же экземпляр
            :return: Laptop(os='_', price=_, screen_size=_  )
            """
            return f"{self.__class__.__name__}(os={self.os!r}, price={self.price}, screen_size={self.screen_size})"
pass
