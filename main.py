import csv


class Item:
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # check valid values
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def apply_discout(self):
        self.price *= self.pay_rate

    @classmethod
    def instanciate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('names'),
                quantity=int(item.get('quantity')),
                price=float(item.get('price')),
            )

    @staticmethod
    def is_integer(num):
        # we will count  out the floats point that are zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return  True

        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"


Item.instanciate_from_csv()
print(Item.is_integer(7.0))
