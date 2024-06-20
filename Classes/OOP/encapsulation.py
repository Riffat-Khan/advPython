class biodata():

    def __init__(self, name, age, city):
        self._name = name # protected "_"
        self.__age = 45  # private "__"
        self.city = city


class next(biodata):

    def __init__(self, name, age, city):
        super().__init__(name, age, city)


    def __print__(self):

        print(self.__age) #    print(self.__age) AttributeError: 'next' object has no attribute '_next__age'
        print(self._name) # None
        



person = next("anil" , 33, "lhr")
print(person.__print__())