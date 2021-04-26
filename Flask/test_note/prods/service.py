import test_note.prods.productDao as pdao

class Service:
    def __init__(self):
        self.dao = pdao.Dao('./products.xls')

    def addProduct(self):
        print('제품추가')
        num = int(input('제품번호:'))
        name = input('제품명:')
        price = int(input('가격:'))
        amount = int(input('수량:'))
        self.dao.insert([num, name, price, amount, 0])

    def printProduct(self):
        print('제품검색')
        num = int(input('제품번호:'))
        res = self.dao.select(num)
        if res.empty:
            print('없는 제품')
        else:
            print(res)

    def getProduct(self, num):
        res = self.dao.select(num)
        if res.empty:
            print('없는 제품')
        else:
            return res

    def editPrice(self):
        print('제품가격 수정')
        num = int(input('제품번호:'))
        price = int(input('새 가격:'))
        self.dao.update('price', num, price)

    def delProduct(self):
        print('제품삭제')
        num = int(input('제품번호:'))
        self.dao.delete(num)

    def getAll(self):
        prods = self.dao.selectAll()
        print(prods)
        return prods

    def in_out(self, type, num, amount):
        print('입출고')
        if type=='out':
            amount = -amount

        p = self.getProduct(num)
        if not p.empty:
            n_amount = p['amount']
            y = n_amount+amount
            if y<0:
                print('수량부족')
            else:
                self.dao.update('amount', num, y)
                if type=='out':
                    k = p['sell_amount']
                    self.dao.update('sell_amount', num, k+(-amount))

    def get_sell_amount(self):
        x = self.dao.selectSellAmount()
        print(x)
