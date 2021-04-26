import pandas as pd
#주문, 주문목록, 결제, 주문취소
class OrderDao:
    def __init__(self, path):
        self.path = path
        self.orders = self.readFile()

    def readFile(self):
        return pd.read_excel(self.path)

    #주문번호(인덱스),제품번호, 주문수량, 결제금액, 결제유무
    def insert(self, o):#['제품번호', '주문수량', '결제금액', '결제유무']
        keys = ['제품번호', '주문수량', '결제금액', '결제유무']
        new_row = {}  # 빈 딕셔너리
        for i in range(0, len(keys)):  # 입력받은 데이터로 딕셔너리 생성
            new_row[keys[i]] = o[i]

        # 생성한 딕셔너리를 데이터 프레임에 한 줄 추가
        self.orders = self.orders.append(new_row, ignore_index=True)

    def selectAll(self):
        return self.orders

    def updatePay(self, idx):#결제
        self.orders.loc[idx, '결제유무']=True

    def delete(self, idx):#주문취소
        self.orders.drop(idx, inplace=True)

    def select(self, idx):
        return self.orders.loc[idx, ['제품번호','주문수량']]