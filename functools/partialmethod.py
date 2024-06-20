from functools import partialmethod
class whatever:

    def __init__(self):
        self.name = "whatever"

    def _name(self, newName):
        self.name = newName     
        
    name_1 = partialmethod(_name , newName = "hey I'm ali")
    name_2 = partialmethod(_name , newName = "hey I'm afifa")


obj = whatever()
obj.name_1()
print(obj.name)
obj.name_2()
print(obj.name)