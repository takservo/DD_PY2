import doctest
from typing import Union


class Table:
    """
    Документация на класс.
    Класс описывает модель стола
    """
    def __init__(self, length: Union[int, float], width: Union[int, float], material: str):
        """
        Создание объекта "стол"

        :param length: Длина стола(см)
        :param width: Ширина стола(см)
        :param material: Материал, из которого изготовлен стол

        Example:
        >>> table1 = Table(100, 70, "дерево")
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int")
        if length < 0:
            raise ValueError("Длина не может быть отрицательной")
        self.length = length
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть типа int")
        if width < 0:
            raise ValueError("Ширина не может быть отрицательной")
        self.width = width
        if not isinstance(material, str):
            raise TypeError("Матриал  должен быть типа str")
        self.matrial = material

    def change_surface_material(self, new_material: str) -> None:
        """
        Функция, меняющая материалл поверхности стола

        :param new_material: Новый материал поверхности стола

        Example:
        >>> table1 = Table(100, 70, "дерево")
        >>> table1.change_surface_material("стекло")
        """
        if not isinstance(new_material, str):
            raise TypeError("Матриал  должен быть типа str")
        ...

    def table_defect(self, defect: str) -> None:
        """
        Функция, описывающая неисправность стола

        :param defect: Неисправность

        Example:
        >>> table1 = Table(100, 70, "дерево")
        >>> table1.table_defect("Сломана ножка")
        """
        if not isinstance(defect, str):
            raise TypeError("Неисправность  должна быть типа str")
        ...


class Laptop:
    """
    Документация на класс.
    Класс описывает модель ноутбука
    """
    def __init__(self, model: str, price: int):
        """
        Создание объекта "ноутбук"

        :param model: Модель ноутбука
        :param price: Цена ноутбука(руб)

        Example:
        >>> laptop1 = Laptop("Lenovo IdeaPad 1", 33000)
        """
        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        self.model = model
        if not isinstance(price, int):
            raise TypeError("Цена должна быть типа int")
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = price

    def sell_laptop(self, sell_price: int) -> None:
        """
        Функция, которая продаёт ноутбук

        :param sell_price: Цена, за которую продаёте ноутбук

        Example:
        >>> laptop1 = Laptop("Lenovo IdeaPad 1", 33000)
        >>> laptop1.sell_laptop(25000)
        """
        if not isinstance(sell_price, int):
            raise TypeError("Цена должна быть типа int")
        ...

    def is_laptop_turned_on(self) -> bool:
        """
        Функция, проверяющая, вкулючен ли ноутбук

        :return: Включён ли ноутбук

        Example:
        >>> laptop1 = Laptop("Lenovo IdeaPad 1", 33000)
        >>> laptop1.is_laptop_turned_on()
        """
        ...


class Magazine:
    """
    Документация на класс.
    Класс описывает модель журнала
    """

    def __init__(self, publisher: str, pages: int, name: str, last_read_page: int):
        """
        Создание объекта "журнал"

        :param publisher: Издатель журнала
        :param pages: Количество страниц в журнале
        :param name: Название журнала
        :param last_read_page: Последняя прочитанная страница

        Example:
        >>> magazine1 = Magazine("Бренд Комьюнити Медиа", 40, "PLAYBOY", 0)
        """
        if not isinstance(publisher, str):
            raise TypeError("Издатель должен быть типа str")
        self.publisher = publisher
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        self.pages = pages
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self.name = name
        if not isinstance(last_read_page, int):
            raise TypeError("Последняя прочитанная страница должна быть типа int")
        if last_read_page < 0:
            raise ValueError("Последняя прочитанная страница не может быть отрицательной")
        if last_read_page > pages:
            raise ValueError("Последняя прочитанная страница не может быть больше общего количства страниц")
        self.last_read_page = last_read_page

    def increment_last_read_page(self, read_pages: int) -> int:
        """
        Функция, которая отслеживает последнюю прочитанную страницу

        :return: Последняя прочитанная страница

        :param read_pages: Количество прочитанных страниц

        Example:
        >>> magazine1 = Magazine("Бренд Комьюнити Медиа", 40, "PLAYBOY", 0)
        >>> magazine1.increment_last_read_page(20)
        """
        if not isinstance(read_pages, int):
            raise TypeError("Количество прочитанных страниц должно быть типа int")
        if read_pages < 0:
            raise ValueError("Количество прочитанных страниц не может быть отрицательным")
        if read_pages > (self.pages - self.last_read_page):
            raise ValueError("Количество прочитанных страниц не может быть больше количества непрочитанных страниц")
        ...

    def is_magazine_read(self) -> bool:
        """
        Функция, проверяющая прочитан ли журнал

        :return: Прочитан ли журнал

        Example:
        >>> magazine1 = Magazine("Бренд Комьюнити Медиа", 40, "PLAYBOY", 0)
        >>> magazine1.is_magazine_read()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
