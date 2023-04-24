class Car:
    """
    Документация на класс.
    Класс описывает модель автомобиля
    """

    def __init__(self, car_brand: str, price: int):
        """
        Создание объекта "автомобиль"(базовый класс)

        :param car_brand: марка автомобиля
        :param price: Цена автомобиля(руб)
        """
        self.car_brand = car_brand
        self.price = price

    def open_door(self, door_number) -> None:
        """
        Метод, открывающий дверь
        :param door_number: номер двери, которую необходимо открыть
        """
        ...

    def is_car_closed(self) -> bool:
        """
        Метод, проверяющий, закрыт ли транспорт
        :return: закрыты ли двери
        """
        ...

    def is_car_running(self) -> bool:
        """
        Функция, проверяющая, заведен ли автомобиль
        :return: заведён ли автомобиль
        """
        ...

    def __str__(self) -> str:
        """
        Метод __str__ должен возвращать строку, где "марка автомобиля" берется с помощью атрибута car_brand,
        "цена" берется с помощью атрибута price
        :return: Автомобиль. Марка автомобиля: марка автомобиля. Цена: цена.
        """
        return f"Автомобиль. Марка автомобиля: {self.car_brand}. Цена: {self.price}."

    def __repr__(self):
        """
        Метод __repr__ должен возвращать валидную python строку,
        по которой можно инициализировать точно такой же экземпляр
        :return: Car(car_brand=_, price=_)
        """
        return f"{self.__class__.__name__}(car_brand={self.car_brand}, price={self.price})"


if __name__ == "__main__":

    class Truck(Car):
        """
        Документация на класс.
        Класс описывает модель грузового автомобиля
        """

        def __init__(self, car_brand: str, price: int, load_capacity: int):

            """
            Создание и подготовка к работе объекта "Truck" (дочерний класс)

            :param car_brand: марка грузового автомобиля
            :param price: Цена грузового автомобиля(руб)
            :param load_capacity: Грузоподъёмность грузового автомобиля
            """

            super().__init__(car_brand, price)
            # Атрибуты price и car_brand наследуются из базового класса
            self.load_capacity = load_capacity

        def is_car_closed(self) -> bool:

            """
            Метод для установки приложения необходимо перегрузить(так как для грузового
            автомобиля есть необходимсоть проверки кузова)
            :return: закрыт ли транспорт
            """
            ...

        def transport_product(self, product_weigh: int) -> None:
            """
            Функция, перевозящая товар в грузовике
            """
            ...

        def __repr__(self) -> str:
            """
            Метод __repr__ должен возвращать валидную python строку,
            по которой можно инициализировать точно такой же экземпляр
            :return: Truck(car_brand='_', price=_, load_capacity=_  )
            """
            return f"{self.__class__.__name__}(car_brand={self.car_brand!r}, price={self.price}, load_capacity={self.load_capacity})"
pass
