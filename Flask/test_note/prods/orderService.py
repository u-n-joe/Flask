import test_note.prods.orderDao as odao
#주문, 주문목록, 결제, 주문취소
class Service:
    def __init__(self):
        self.dao = odao.OrderDao('orders.xls')

    def mkOrder(self):
        print('order')
        num = int(input('주문할 제품 번호:'))
        amount = int(input('주문 수량:'))

        return num, amount

    def addOrder(self, d):#d:(제품번호, 단가, 수량)
        m = d[1]*d[2]#price*수량: 결제금액
        #['제품번호', '주문수량', '결제금액', '결제유무']
        self.dao.insert([d[0], d[2], m, False])

    def getAll(self):
        orders = self.dao.selectAll()
        print(orders)
        return orders

    def delOrder(self):#결제 안한 것만 취소 가능. 결제유무가 False인것만 추출
        o = self.getAll()
        idx = int(input('취소할 주문 인덱스(결제유무가 False인것만 입력):'))
        if o.loc[idx, '결제유무']=='True':
            print('이미 결제한 상품은 취소 불가')
        else:
            self.dao.delete(idx)

    def pay(self):
        o = self.getAll()
        idx = int(input('결제할 주문 인덱스(결제유무가 False인것만 입력):'))
        if o.loc[idx, '결제유무'] == 'True':
            print('이미 결제한 상품')
        else:
            self.dao.updatePay(idx)

    def mkOut(self):
        self.getAll()
        idx = int(input('출고할 주문 번호:'))
        return self.dao.select(idx)
