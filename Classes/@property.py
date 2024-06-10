class house:

    def __init__(self , price):
        self._price = price    #_price === protected

    @property
    #getting the price
    def price(self):
        return self._price
    

    #setting the new value
    @price.setter
    def price(self , new_price):
        if new_price > 0 and isinstance(new_price , int):
            self._price = new_price
        else: return self.price

    #deleting the price
    @price.deleter
    def price(self):
        del self._price


house1 = house(500000)
house1.price = 1000000
print(house1.price)