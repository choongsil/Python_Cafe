class Menu:
    def __init__(self):
        self.name=[]
        self.price=[]
        #menu.txt 를 읽어서, name, price  로 분리한후
        #self.name , self.price 에 추가하고 close
    def read(self):
        f = open('d:/temp/menu.txt', mode='r', encoding='utf-8')
        lines = f.readlines()
        for row in lines:
            ar = row.split(",")
            self.name=ar[0]
            self.price=ar[1]
        f.close()

    def display(self):
        for i in range(len(self.name)):
            print(self.name[i], ",", self.price[i])

    def addnew(self,name,price):
        self.name.append(name)
        self.price.append(price)

    def update(self, ndx, name, price):
        self.name[ndx]=name
        self.price[ndx]=price

    def delete(self, ndx):
        del self.name[ndx]
        del self.price[ndx]

    def save(self):
        #self.name , self.price  의 값을 menu.txt에 쓰기하고 close
        f = open('d:/temp/menu.txt', mode='w', encoding='utf-8')
        f.writelines([self.name, ',',self.price, '\n'])
        f.close()