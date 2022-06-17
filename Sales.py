from Order import Order
order=Order()
class Sales():
    def __init__(self):
        self.mobile=[]
        self.total= []
        self.created=[]
    def add(self, mobile, price, date):
        self.mobile.append(mobile)
        self.total.append(price)
        self.created.append(date)

    def sum(self):
        #매출목록 보여주고
        print('매출목록')
        for i in range(len(self.mobile)):
            print(self.mobile[i], self.total[i],'원',self.created[i])
        #매출총액계산/출력
        print('매출 총액')
        print(sum(self.total),'원')
