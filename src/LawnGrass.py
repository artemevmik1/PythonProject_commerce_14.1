from src.Product import Product


class LawnGrass(Product):
    """Газонная трава — наследник Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country  # страна-производитель
        self.germination_period = germination_period  # срок прорастания
        self.color = color  # цвет

    def __str__(self):
        return (
            f"Газонная трава «{self.name}» ({self.color}), "
            f"страна: {self.country}, срок прорастания: {self.germination_period}, "
            f"цена: {self.price} руб."
        )
