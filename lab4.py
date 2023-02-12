if __name__ == "__main__":
    class Laptop:
        """
        Документация на класс.
        Класс описывает модель ноутбука
        """

        def __init__(self, screen_size: int, price: int):
            """
            Создание объекта "ноутбук"(базовый класс)

            :param screen_size: Диагональ экрана ноутбука
            :param price: Цена ноутбука(руб)
            """
            self.screen_size = screen_size
            self.price = price

        def set_laptop_sell_price(self, sell_price: int) -> int:
            """
            Метод, задающий цену продажи ноутбука

            :param sell_price: Цена, за которую продаёте ноутбук
            :return sell_price: Цена продажи
            """
            ...

        def install_app(self, app: str) -> None:
            """
            Метод, устанавливающий приложение на ноутбук

            :param app: приложение, устанавливаемое на ноутюбук
            """
            ...

        def is_laptop_on(self) -> bool:
            """
            Функция, проверяющая, вкулючен ли ноутбук
            :return: Включён ли ноутбук
            """
            ...

        def __str__(self) -> str:
            """
            Метод __str__ должен возвращать строку, где "диагональ экрана" берется с помощью атрибута screen_size,
            "цена" берется с помощью атрибута price
            :return: Ноутбук. Диагональ экрана: диагональ. Цена: цена.
            """
            return f"Ноутбук. Диагональ экрана: {self.screen_size}. Цена: {self.price}."

        def __repr__(self):
            """
            Метод __repr__ должен возвращать валидную python строку,
            по которой можно инициализировать точно такой же экземпляр
            :return: Laptop(screen_size=_, price=_)
            """
            return f"{self.__class__.__name__}(screen_size={self.screen_size}, price={self.price})"

    class MacBook(Laptop):
        """
        Документация на класс.
        Класс описывает модель макбука
        """
        def __init__(self, screen_size: int, price: int, os: str):
            """
            Создание и подготовка к работе объекта "MacBook" (дочерний класс)

            :param screen_size: Диагональ экрана ноутбука
            :param price: Цена ноутбука(руб)
            :param os: Операционная система
            """
            super().__init__(screen_size, price)
            # Атрибуты screen_size, price наследуются из базового класса
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
            :return: Macbook(screen_size=_, price=_, os='_')
            """
            return f"{self.__class__.__name__}(screen_size={self.screen_size}, price={self.price}, os={self.os!r})"
    pass
