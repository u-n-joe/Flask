import test_note.prods.service as pserv
import test_note.prods.orderService as oserv

class Menu:
    def __init__(self):
        self.pserv = pserv.Service()
        self.oserv = oserv.Service()

    def prun(self):#product run
        while True:
            mm = int(input('1.추가 2.검색 3.수정 4.입고 5.출고 6.삭제 7.전체목록 8.판매실적보고 9.종료'))
            if mm==1:
                self.pserv.addProduct()
            elif mm==2:
                self.pserv.printProduct()
            elif mm == 3:
                self.pserv.editPrice()
            elif mm == 4:
                self.pserv.getAll()
                num = int(input('제품번호:'))
                amount = int(input('수량:'))
                self.pserv.in_out('in', num, amount)
            elif mm == 5:
                d = self.oserv.mkOut()
                self.pserv.in_out('out', d[0], d[1])
            elif mm == 6:
                self.pserv.delProduct()
            elif mm == 7:
                self.pserv.getAll()
            elif mm == 8:
                self.pserv.get_sell_amount()
            elif mm == 9:
                break

    def orun(self):#order run
        while True:
            mm = int(input('1.주문 2.주문목록 3.주문취소 4.결제 5.종료'))
            if mm == 1:
                self.pserv.getAll()
                num, amount = self.oserv.mkOrder()
                p = self.pserv.getProduct(num)
                if not p.empty:
                    d = (p['num'], p['price'], amount)
                    self.oserv.addOrder(d)
                else:
                    print('없는 제품 번호')
            elif mm == 2:
                self.oserv.getAll()
            elif mm == 3:
                self.oserv.delOrder()
            elif mm == 4:
                self.oserv.pay()
            elif mm == 5:
                break

    def run(self):#전체 run
        while True:
            mm = int(input('1.공장 2.주문 3.종료'))
            if mm == 1:
                self.prun()
            elif mm==2:
                self.orun()
            elif mm==3:
                break