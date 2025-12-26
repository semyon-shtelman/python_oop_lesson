from src.product import Product


class Category:
    name: str  # название
    description: str  # описание
    products: list  # список товаров категории

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        all_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {all_quantity} шт."

    @property
    def products(self):
        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return str_product

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        self.product_count += 1
