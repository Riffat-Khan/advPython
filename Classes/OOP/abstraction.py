from abc import ABC, abstractmethod

class shape():

    @abstractmethod
    def noOfSides(self):
        pass 

class sqr(shape):
    
    def noOfSides(self):
        return "4"
    
class oct(shape):
    
    def noOfSides(self):
        return "8"
    

shape_1 = sqr().noOfSides()
shape_2 = oct().noOfSides()

print(shape_1)
print(shape_2)