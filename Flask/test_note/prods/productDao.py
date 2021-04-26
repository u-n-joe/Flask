import pandas as pd

class Dao:#저장소 저장, 검색, 수정, 삭제
    def __init__(self, path):
        self.path = path#엑셀 파일 경로
        self.prods = self.readFile()#엑셀 파일에서 데이터 읽어서 데이터프레임으로 저장


    def readFile(self):
        return pd.read_excel(self.path)

    def insert(self, p):#p는 서비스에서 제품명, 가격, 수량을 입력받아 []로 전달
        # 이 메서드에 파라메터로 넣어서 호출
        print('제품추가. p는 Product 객체')
        keys = ['num','name', 'price', 'amount', 'sell_amount']
        new_row = {} #빈 딕셔너리
        for i in range(0, len(keys)):#입력받은 데이터로 딕셔너리 생성
            new_row[keys[i]]=p[i]

        #생성한 딕셔너리를 데이터 프레임에 한 줄 추가
        self.prods = self.prods.append(new_row, ignore_index=True)

    def getIdx(self, num):
        idx = self.prods[self.prods['num'] == num].index
        return idx[0]

    def select(self, num):#제품번호로 검색하여 그 위치 반환
        idx = self.getIdx(num)
        print(idx)
        return self.prods.loc[idx, :]

    def update(self, col, num, val):#제품 가격만 수정
        idx = self.getIdx(num)
        self.prods.loc[idx, col]=val

    def delete(self, num):
        idx = self.getIdx(num)
        self.prods.drop(idx, inplace=True)#인덱스가 num인 행을 삭제

    def selectAll(self):
        return self.prods

    def selectSellAmount(self):
        return self.prods[['num','name','sell_amount']]