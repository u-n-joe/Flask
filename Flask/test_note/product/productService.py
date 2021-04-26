import test_note.product.productDao as dao
import test_note.product.productVO as prod

class Service:
    def __init__(self):
        self.dao = dao.Dao()

    def addProduct(self):
        print('제품명, 가격, 수량 입력받아 Product객체 생성 후 dao.insert()로 추가')
        name = input('제품명:')
        price = int(input('price:'))
        a = int(input('amount:'))

        self.dao.insert(prod.Product(name, price, a))

    def getProduct(self):
        print('검색할 번호 입력받아 dao.select()로 검색')
        num = int(input('num:'))
        res = self.dao.select(num)
        if res==None:
            print('없는 제품')
        else:
            res[1].printProduct()

    def editProduct(self):
        print('수정할 제품 번호와 새 가격 입력받아 dao.update()로 수정')
        num = int(input('num:'))
        price = int(input('new price:'))
        p = prod.Product('', price, 0)
        p.num = num
        self.dao.update(p)

    def delProduct(self):
        print('삭제할 제품 번호 입력받아 dao.delete()로 삭제')
        num = int(input('num:'))
        self.dao.delete(num)

    def printAll(self):
        print('dao.selectAll()로 전체 검색한 결과 출력')
        datas = self.dao.selectAll()
        for p in datas:
            p.printProduct()