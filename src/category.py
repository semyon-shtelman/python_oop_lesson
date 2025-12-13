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

    @property
    def products(self):
        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return str_product


    def add_product(self, product):
        self.__products.append(product)
        self.product_count += 1
