from src.Product import Product


class Smartphone(Product):
    """Смартфон — наследник Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency  # производительность
        self.model = model  # модель
        self.memory = memory  # объём встроенной памяти, ГБ
        self.color = color  # цвет

    def __str__(self):
        return (
            f"Смартфон {self.model} ({self.color}), "
            f"память {self.memory} ГБ, производительность: {self.efficiency}, "
            f"цена: {self.price} руб."
        )
