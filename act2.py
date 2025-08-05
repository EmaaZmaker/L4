class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("SELLING PRICE IS....",self.__maxprice)
    def set_maxprice(self,price):
        self.__maxprice=price
obj1=computer()
obj1.sell()
obj1.__maxprice=1000
obj1.sell()
obj1.set_maxprice(1000)
obj1.sell()
        
        