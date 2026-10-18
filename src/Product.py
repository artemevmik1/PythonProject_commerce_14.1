class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = value

    @classmethod
    def new_product(cls, product_data: dict, products: list = None):
        """Создаёт товар из словаря, учитывая дубликаты в products."""
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        # перебираем существующие товары
        if products:
            for existing in products:
                if existing.name == name:
                    # количество складываем
                    existing.quantity += quantity
                    # цену берём максимальную
                    existing.price = max(existing.price, price)
                    return existing

        # дубликата нет — создаём новый товар
        return cls(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
        )



