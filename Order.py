class Order:
    def __init__(self):
        self.menu_no=[]
        self.qty=[]
        self.price=[]
    def add(self, menu_no, qty, price):
        self.menu_no.append(menu_no-1)
        self.qty.append(qty)
        self.price.append(price*qty)

    def cancel(self):
        self.menu_no.clear()
        self.qty.clear()
        self.price.clear()