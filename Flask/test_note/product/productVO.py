class Product:
    def __init__(self,num=None, name=None, price=None, amount=None, sell_amount=None):#객체가 생성 될때마다 호출됨
        self.num = num
        self.name = name
        self.price = price
        self.amount = amount
        self.sell_amount = sell_amount

    def printProduct(self):
        print('num:', self.num)
        print('name:', self.name)
        print('price:', self.price)
        print('amount:', self.amount)