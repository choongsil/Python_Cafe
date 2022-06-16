class Menu:
    def __init__(self):
        self.name=[]
        self.price=[]
        #menu.txt 를 읽어서, name, price  로 분리한후
        #self.name , self.price 에 추가하고 close
        f = open("d:/temp/menu.txt", mode='r', encoding='utf-8')
        lines = f.readline()
        while lines!='':
            ar = lines.split(",")
            self.name.append(ar[0])
            self.price.append(int(ar[1]))
            lines=f.readline()
        f.close()

    def display(self):
        for i in range(len(self.name)):
            print(self.name[i], ",", self.price[i])

    def addnew(self, name, price):
        self.name.append(name)
        self.price.append(str(price))

    def update(self, ndx, name, price):
        self.name[ndx]=name
        self.price[ndx]=str(price)

    def delete(self, ndx):
        del self.name[ndx]
        del self.price[ndx]

    def save(self):
        #self.name , self.price  의 값을 menu.txt에 쓰기하고 close
        f = open("d:/temp/menu.txt", mode='w', encoding='utf-8')
        for i in range(len(self.name)):
            f.writelines([str(self.name[i]), ',', str(self.price[i]),'\n'])
        f.close()

menu=Menu()
# menu.addnew('모카',3000)
# print(menu.name)
# print(menu.price)
# menu.update(0, '라떼', 5000)
menu.delete(1)
menu.save()
menu.display()
print("----------")

