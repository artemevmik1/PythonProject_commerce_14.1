from src.Product import Product


class Category:
    name: str
    description: str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products) if products is not None else 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity}"

    def add_product(self, product):
        """Добавляет товар в категорию. Принимает только Product и его наследников."""
        if not isinstance(product, Product):
            raise TypeError(
                f"В категорию можно добавить только Product или его наследника, " f"а получен {type(product).__name__}"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает строку со всеми товарами категории."""
        return "\n".join(str(product) for product in self.__products)
