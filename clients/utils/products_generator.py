from clients.models.order import Product


class ProductsGenerator:
    def list_products(self):
        return [
            dict(name='Xbox Series S', price=2700, description=''),
            dict(name='Xbox Series X', price=5000, description=''),
            dict(name='PS5', price=5500, description=''),
            dict(name='Monitor', price=1000, description=''),
            dict(name='Notebook', price=4500, description=''),
            dict(name='Mouse', price=60, description=''),
            dict(name='Teclado', price=120, description=''),
            dict(name='Phone', price=120, description=''),
            dict(name='Phone Bluetooth', price=280, description=''),
            dict(name='Pen drive 32GB', price= 50, description=''),
            dict(name='Celular', price=1000, description=''),
            dict(name='Garrafa Térmica', price=40, description=''),

        ]

    def create_products(self):
        try:
            list_product = []
            for product in self.list_products():
                data = Product(**product)
                list_product.append(data)

            return list_product
        except Exception as e :
            print('error', e)

