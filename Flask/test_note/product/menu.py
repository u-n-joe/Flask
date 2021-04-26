import test_note.product.productService as serv

class Menu:
    def __init__(self):
        self.service = serv.Service()

    def run(self):
        while True:
            x = int(input('1.제품추가 2.제품검색 3.제품수정 4.제품삭제 5.전체목록 6.종료'))
            if x==1:
                self.service.addProduct()
            elif x==2:
                self.service.getProduct()
            elif x==3:
                self.service.editProduct()
            elif x==4:
                self.service.delProduct()
            elif x==5:
                self.service.printAll()
            elif x==6:
                break