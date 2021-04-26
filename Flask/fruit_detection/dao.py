import pandas as pd
import pkg_resources
import xlrd

class Product:
    # 객체가 생성 될때마다 호출
    def __init__(self, num=None, name=None, price=None, amount=None, sell_amount=None):
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

def getAll():
    list = []
    pp = xlrd.open_workbook('items.xls')
    # pp = pkg_resources.resource_filename('fruit_detection', 'items.xls')
    datas = pd.read_excel(pp, index_col=None)
    i = 0
    while True:
        try:
            num = datas.loc[i, 'num']
            name = datas.loc[i, 'name']
            price = datas.loc[i, 'price']
            amount = datas.loc[i, 'amount']
            # print(num, name, price, amount)
            p = Product(num=num, name=name, price=price, amount=amount)
            p.printProduct()
            list.append(p)
        except KeyError:
            print('key error')
            break
        i += 1
    return list